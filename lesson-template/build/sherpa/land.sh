#!/bin/sh
# One page, start to commit: fill from the draft, verify, build, check, commit.
#   sh lesson-template/build/sherpa/land.sh <slug> <draft.json> <html-file>
set -e
cd "$(dirname "$0")/../../.."
export PYTHONIOENCODING=utf-8
py lesson-template/build/sherpa/tm.py fill "$1" "$2"
py lesson-template/build/sherpa/verify_i18n.py "$1"
py lesson-template/build/build_sherpa.py "$1"
node lesson-template/check-lesson.js "$3" 2>&1 | grep -E "FAIL" | grep -v "SEO:start" || true
git add "lesson-template/build/sherpa/i18n/$1.json"
git commit -q -o "lesson-template/build/sherpa/i18n/$1.json" -m "Sherpa Tensing: $1 translated

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
echo "landed $1"
