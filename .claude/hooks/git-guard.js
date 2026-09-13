#!/usr/bin/env node
'use strict';
// PreToolUse guard for the Bash and PowerShell tools.
//
// This checkout is shared by several live Claude sessions at once. Each one
// sees the others' half-finished files in `git status`. The commands below
// either destroy a peer's uncommitted work (stash, reset --hard, clean,
// checkout ., restore .), sweep it into your commit (add -A, add <dir>,
// commit -a, a bare commit of the whole index, --amend), or move the whole
// tree out from under everyone (checkout <branch>, switch). None of them is
// ever the right call in the main tree, so the harness refuses them here
// rather than trusting each session to remember. See CLAUDE.md, "Several
// sessions share this tree", and docs/HANDOFF.md 2026-09-09 "Three sessions,
// one index" for the incidents that made this necessary.
//
// Exit 2 + stderr = block; the message goes back to the model.
// Exit 0 = allow. Anything unexpected (no JSON, no command) = allow.
//
// Inside a linked worktree (`git worktree add ...`) the guard stands down:
// that tree belongs to one session and normal git applies there.
//
// Self-test:  node .claude/hooks/git-guard.js --test

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

function main(raw) {
  let cmd = '';
  try {
    const j = JSON.parse(raw);
    cmd = String((j.tool_input && j.tool_input.command) || '');
  } catch (e) {
    return 0;
  }
  if (!/\bgit\b/.test(cmd)) return 0;
  if (inLinkedWorktree()) return 0;
  const hit = firstViolation(cmd);
  if (!hit) return 0;
  process.stderr.write(explain(hit));
  return 2;
}

function inLinkedWorktree() {
  try {
    const r = spawnSync('git', ['rev-parse', '--git-dir', '--git-common-dir'],
      { encoding: 'utf8', timeout: 5000 });
    if (r.status !== 0) return false;
    const [gitDir, common] = r.stdout.trim().split(/\r?\n/);
    return path.resolve(gitDir) !== path.resolve(common);
  } catch (e) {
    return false;
  }
}

// Split a shell line into simple commands on the separators both shells share.
function segments(cmd) {
  return cmd.split(/\r?\n|&&|\|\||;|\|(?!\|)/).map(s => s.trim()).filter(Boolean);
}

// Tokenise loosely: quotes are honoured, nothing else is interpreted.
function tokens(seg) {
  const out = [];
  const re = /"([^"]*)"|'([^']*)'|(\S+)/g;
  let m;
  while ((m = re.exec(seg))) {
    out.push(m[1] !== undefined ? m[1] : m[2] !== undefined ? m[2] : m[3]);
  }
  return out;
}

const GLOBAL_WITH_ARG = new Set(['-C', '-c', '--git-dir', '--work-tree', '--namespace', '--exec-path']);

function gitInvocation(seg) {
  const t = tokens(seg);
  let i = t.findIndex(x => x === 'git' || /[\\/]git(\.exe)?$/i.test(x));
  if (i < 0) return null;
  i += 1;
  const globals = [];
  while (i < t.length && t[i].startsWith('-')) {
    const g = t[i];
    globals.push(g);
    if (GLOBAL_WITH_ARG.has(g)) { globals.push(t[i + 1] || ''); i += 2; } else { i += 1; }
  }
  if (i >= t.length) return null;
  return { sub: t[i], args: t.slice(i + 1), globals };
}

// Options that swallow the next token, per subcommand, so it is not mistaken
// for a pathspec.
const OPT_WITH_ARG = {
  commit: new Set(['-m', '--message', '-F', '--file', '-C', '--reuse-message', '-c', '--reedit-message',
    '--author', '--date', '-t', '--template', '--fixup', '--squash', '--trailer', '--cleanup']),
  checkout: new Set(['-b', '-B', '--orphan', '--conflict', '--pathspec-from-file']),
  restore: new Set(['-s', '--source', '--conflict', '--pathspec-from-file']),
  add: new Set(['--chmod', '--pathspec-from-file']),
  reset: new Set(['--pathspec-from-file']),
};

function positionals(sub, args) {
  const dd = args.indexOf('--');
  if (dd >= 0) return args.slice(dd + 1);
  const swallow = OPT_WITH_ARG[sub] || new Set();
  const out = [];
  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a.startsWith('-')) {
      if (swallow.has(a)) i += 1;           // skip the option's value
      continue;
    }
    out.push(a);
  }
  return out;
}

function isDirOrSweep(p) {
  if (['.', '..', '*', ':/', './', '.\\', ':', '-A', '--all', '-u', '--update'].includes(p)) return true;
  if (/[\\/]$/.test(p) || /\*/.test(p)) return true;
  try { return fs.statSync(p).isDirectory(); } catch (e) { return false; }
}

function isExistingPath(p) {
  try { fs.statSync(p); return true; } catch (e) { return false; }
}

// `-am`, `-sa` and friends: a bundled short flag that contains `a`.
function bundledAll(flags) {
  return flags.some(f => /^-[a-zA-Z]+$/.test(f) && f.includes('a'));
}

function firstViolation(cmd) {
  for (const seg of segments(cmd)) {
    const g = gitInvocation(seg);
    if (!g) continue;
    const { sub, args, globals } = g;
    const flags = args.filter(a => a.startsWith('-'));
    const has = f => flags.includes(f);
    const pos = positionals(sub, args);
    const dd = args.indexOf('--');

    if (globals.some(x => /autostash/i.test(x))) return rule('autostash', seg);
    if (has('--help') || has('-h')) continue;

    switch (sub) {
      case 'stash':
        if (args[0] === 'list' || args[0] === 'show') break;
        return rule('stash', seg);
      case 'reset':
        if (has('--hard') || has('--merge')) return rule('reset', seg);
        break;
      case 'clean':
        return rule('clean', seg);
      case 'checkout': {
        if (has('-b') || has('-B') || has('--orphan') || has('--detach')) return rule('switch', seg);
        if (has('-f') || has('--force')) return rule('discard-all', seg);
        if (pos.some(isDirOrSweep)) return rule('discard-all', seg);
        if (dd >= 0) break;                                  // git checkout [-- ] <file>: path-scoped
        if (pos.length && pos.every(isExistingPath)) break;  // file paths, allowed
        if (pos.length) return rule('switch', seg);          // a ref: branch switch
        break;
      }
      case 'switch':
        return rule('switch', seg);
      case 'restore': {
        if (has('--staged') && !has('--worktree') && !has('-W')) break;   // unstaging is harmless
        if (pos.length === 0 || pos.some(isDirOrSweep)) return rule('discard-all', seg);
        break;
      }
      case 'add': {
        if (has('-A') || has('--all') || has('-u') || has('--update') || bundledAll(flags)) return rule('add-all', seg);
        if (has('-p') || has('--patch') || has('-i') || has('--interactive') || has('-e') || has('--edit')) break;
        if (pos.some(isDirOrSweep)) return rule('add-dir', seg);
        break;
      }
      case 'commit': {
        if (has('--amend')) return rule('amend', seg);
        if (has('-a') || has('--all') || bundledAll(flags)) return rule('commit-all', seg);
        if (has('-i') || has('--include')) return rule('commit-bare', seg);
        if (pos.length === 0) return rule('commit-bare', seg);
        if (!has('-o') && !has('--only')) return rule('commit-bare', seg);
        break;
      }
      case 'rebase':
      case 'pull':
      case 'merge':
        if (has('--autostash')) return rule('autostash', seg);
        break;
      case 'worktree':
        if (args[0] === 'remove' && (has('-f') || has('--force'))) return rule('worktree-force', seg);
        break;
      default:
        break;
    }
  }
  return null;
}

function rule(kind, seg) { return { kind, seg }; }

const WHY = {
  'stash': 'git stash moves EVERY uncommitted change in the tree, including other sessions\' half-finished lessons, and a later `stash pop` or `drop` by anyone loses them. It has already cost this repo four artwork folders once and a three-day-old orphan stash the second time.',
  'reset': 'git reset --hard/--merge discards every uncommitted change in the tree, not just yours.',
  'clean': 'git clean deletes untracked files. A peer\'s not-yet-committed artwork and builders look exactly like clutter.',
  'discard-all': 'This discards working-tree changes for a whole directory or the whole tree. Other sessions\' edits live there too.',
  'switch': 'The main tree is on `main` and every live session assumes so. Switching branches here moves everyone\'s tree and makes their next commit land on your branch.',
  'add-all': 'git add -A / --all / -u stages everything, including files another session is still editing. HANDOFF records commits that swept a peer\'s work this way.',
  'add-dir': 'git add <directory> stages every changed file under it, including a peer\'s. Name the files.',
  'commit-all': 'git commit -a stages every tracked modification in the tree, not only yours.',
  'commit-bare': 'A bare `git commit` commits the whole index. There is ONE index for every live session, so whatever a peer has staged in the last few minutes goes out under your message (HANDOFF 2026-09-09, twice in one afternoon).',
  'amend': 'The last commit on `main` may be another session\'s. --amend rewrites it, and any pushed history.',
  'autostash': '--autostash stashes and re-applies every peer\'s uncommitted change around your operation; a conflict on re-apply drops it.',
  'worktree-force': 'worktree remove --force deletes a worktree with uncommitted changes in it. Check it is empty first.',
};

const INSTEAD = {
  'stash': 'Commit your own files by name (`git add <file>...` then `git commit -o <file>... -m "..."`), or do the work in a worktree: `git worktree add ../FORBES-<task> -b <task>`.',
  'reset': 'Undo your own change with `git checkout -- <file>` (path-scoped is allowed). Leave files you did not touch alone; they are a peer\'s.',
  'clean': 'Delete only the specific files you created: `rm <file>`. Leave the rest.',
  'discard-all': 'Name the file: `git checkout -- <file>` or `git restore <file>`, after `git diff <file>` to confirm the change is yours.',
  'switch': 'Stay on `main`. For a branch, use a worktree: `git worktree add ../FORBES-<task> -b <task>`; git is unrestricted inside it. Merge back to main and `git worktree remove` it when done.',
  'add-all': 'Stage by file name: `git add <file> <file>...`. Then `git diff --cached --name-only` must list only your files.',
  'add-dir': 'Stage by file name: `git add <file> <file>...` (`git status --short <dir>` shows what is there; only your own files go in).',
  'commit-all': 'Stage by name, then `git commit -o <file>... -m "..."` so nothing a peer staged rides along.',
  'commit-bare': 'Name what you are committing: `git commit -o <file> <file>... -m "..."`. -o commits exactly those paths and ignores the rest of the index. New files still need `git add <file>` first. A directory you created (a new artwork folder) may be given as one path.',
  'amend': 'Make a new commit instead.',
  'autostash': 'Commit your own files first, then `git pull --rebase` (git refuses while the tree has unstaged changes; a plain `git pull` merges around them).',
  'worktree-force': 'Run `git -C <worktree> status --short` first; if it prints nothing, `git worktree remove` without --force works.',
};

function explain(hit) {
  return [
    'BLOCKED by .claude/hooks/git-guard.js: this checkout is shared by several live Claude sessions.',
    'Command: ' + hit.seg,
    'Why: ' + WHY[hit.kind],
    'Instead: ' + INSTEAD[hit.kind],
    'Rules: CLAUDE.md, "Several sessions share this tree".',
    '',
  ].join('\n');
}

function selfTest() {
  const cases = [
    // [command, expected rule or null]
    ['git status', null],
    ['git stash list', null],
    ['git stash show -p', null],
    ['git stash', 'stash'],
    ['git stash -u', 'stash'],
    ['git stash push -m x', 'stash'],
    ['git stash pop', 'stash'],
    ['cd /c/x && git stash', 'stash'],
    ['git reset --hard', 'reset'],
    ['git reset --hard origin/main', 'reset'],
    ['git reset HEAD -- library.html', null],
    ['git reset', null],
    ['git clean -fd', 'clean'],
    ['git checkout -- CLAUDE.md', null],
    ['git checkout CLAUDE.md', null],
    ['git checkout -- .', 'discard-all'],
    ['git checkout .', 'discard-all'],
    ['git checkout -- docs/', 'discard-all'],
    ['git checkout docs', 'discard-all'],
    ['git checkout main', 'switch'],
    ['git checkout -b feature', 'switch'],
    ['git checkout origin/main -- library.html', null],
    ['git switch main', 'switch'],
    ['git switch -c x', 'switch'],
    ['git restore CLAUDE.md', null],
    ['git restore .', 'discard-all'],
    ['git restore --staged CLAUDE.md', null],
    ['git restore --staged --worktree .', 'discard-all'],
    ['git add CLAUDE.md docs/HANDOFF.md', null],
    ['git add -A', 'add-all'],
    ['git add --all', 'add-all'],
    ['git add -u', 'add-all'],
    ['git add .', 'add-dir'],
    ['git add docs', 'add-dir'],
    ['git add -A -- lesson-template block-camp', 'add-all'],
    ['git add -p', null],
    ['git commit -m "x"', 'commit-bare'],
    ['git commit', 'commit-bare'],
    ['git commit -a -m "x"', 'commit-all'],
    ['git commit -am "x"', 'commit-all'],
    ['git commit --amend --no-edit', 'amend'],
    ['git commit -o CLAUDE.md -m "x"', null],
    ['git commit -o -m "x" CLAUDE.md docs/HANDOFF.md', null],
    ['git commit -o -- CLAUDE.md -m "x"', null],
    ['git commit -m "x" CLAUDE.md', 'commit-bare'],
    ['git commit -o -F msg.txt CLAUDE.md', null],
    ['git commit -i CLAUDE.md -m x', 'commit-bare'],
    ['git pull --rebase', null],
    ['git pull --rebase --autostash', 'autostash'],
    ['git -c rebase.autoStash=true pull --rebase', 'autostash'],
    ['git rebase origin/main', null],
    ['git merge origin/main', null],
    ['git push', null],
    ['git worktree add ../FORBES-x -b x', null],
    ['git worktree remove ../FORBES-x', null],
    ['git worktree remove --force ../FORBES-x', 'worktree-force'],
    ['git log --oneline | head', null],
    ['git diff --cached --name-only', null],
    ['py tools/seo.py && git add library.html && git commit -o library.html -m "seo"', null],
    ['py tools/seo.py && git add library.html && git commit -m "seo"', 'commit-bare'],
    ['echo "git stash" > note.txt', null],      // a quoted mention is not a command
    ['git --help', null],
    ['git stash --help', null],
  ];
  let bad = 0;
  for (const [cmd, want] of cases) {
    const hit = firstViolation(cmd);
    const got = hit ? hit.kind : null;
    const ok = got === want;
    if (!ok) bad += 1;
    console.log((ok ? 'ok   ' : 'FAIL ') + JSON.stringify(cmd) + '  -> ' + got + (ok ? '' : '  (wanted ' + want + ')'));
  }
  console.log(bad ? bad + ' failure(s)' : 'all ' + cases.length + ' cases pass');
  return bad ? 1 : 0;
}

if (require.main === module) {
  if (process.argv.includes('--test')) process.exit(selfTest());
  let raw = '';
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', d => { raw += d; });
  process.stdin.on('end', () => { process.exit(main(raw)); });
  // If nothing ever arrives on stdin, do not hang the tool call.
  setTimeout(() => process.exit(0), 4000).unref();
}

module.exports = { firstViolation, segments };
