import React, { useState, useEffect, useMemo, useCallback } from 'react';
import {
  BookOpen,
  CheckCircle2,
  XCircle,
  ArrowRight,
  RotateCcw,
  Search,
  X,
  Lightbulb,
  Flame,
  Trophy,
  AlertTriangle,
  Scale,
  Sparkles,
  Timer,
  Filter,
  Gamepad2,
  GraduationCap,
  RefreshCw,
  Eye,
  EyeOff,
  Hammer,
  Clock
} from 'lucide-react';

// ============================================================================
// 1. CATEGORIES & MINECRAFT VOXEL INLINE SVG ARTWORK
// ============================================================================

const CATEGORIES = [
  {
    id: 'regular',
    labelDE: 'Regelmäßig',
    fullTitleDE: 'Regelmäßige Verben (-ed)',
    iconType: 'wood-plank',
    descDE: '-ed, y → ied & Doppelkonsonant'
  },
  {
    id: 'irregular',
    labelDE: 'Unregelmäßig',
    fullTitleDE: 'Unregelmäßige Verben (2. Form)',
    iconType: 'anvil',
    descDE: 'built, dug, found, went, fought...'
  },
  {
    id: 'neg_quest',
    labelDE: "Fragen & didn't",
    fullTitleDE: "Verneinung & Fragen (did / didn't)",
    iconType: 'redstone-torch',
    descDE: "didn't + Grundform, Did you...?"
  },
  {
    id: 'was_were',
    labelDE: 'was / were',
    fullTitleDE: 'was / were & could',
    iconType: 'shield',
    descDE: 'I was, you were, There was/were'
  },
  {
    id: 'traps',
    labelDE: 'Deutsch-Fallen',
    fullTitleDE: 'Signalwörter & Deutsch-Fallen',
    iconType: 'creeper',
    descDE: 'yesterday, ago & keine Perfekt-Falle'
  }
];

const CATEGORY_MAP = CATEGORIES.reduce((acc, cat) => {
  acc[cat.id] = cat;
  return acc;
}, {});

/**
 * Hero Banner SVG: Minecraft Overworld & Ancient Ruins with Time Portal
 * Includes voxel grass blocks, oak trees, blocky clouds, pixel moon/sun,
 * Creeper silhouette, glowing diamond pickaxe, and an obsidian TIME PORTAL frame.
 */
const OverworldTimePortalSVG = () => (
  <svg
    viewBox="0 0 1200 230"
    className="w-full h-40 sm:h-48 md:h-56 object-cover select-none pointer-events-none"
    preserveAspectRatio="xMidYMax slice"
    aria-hidden="true"
  >
    <defs>
      <linearGradient id="psSky" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stopColor="#090b10" />
        <stop offset="55%" stopColor="#131926" />
        <stop offset="100%" stopColor="#1d2433" />
      </linearGradient>
      <linearGradient id="portalSwirl" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stopColor="#38bdf8" stopOpacity="0.85" />
        <stop offset="50%" stopColor="#9333ea" stopOpacity="0.9" />
        <stop offset="100%" stopColor="#4f46e5" stopOpacity="0.85" />
      </linearGradient>
      <radialGradient id="portalGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#a855f7" stopOpacity="0.45" />
        <stop offset="60%" stopColor="#38bdf8" stopOpacity="0.16" />
        <stop offset="100%" stopColor="#111318" stopOpacity="0" />
      </radialGradient>
    </defs>

    {/* Sky */}
    <rect width="1200" height="230" fill="url(#psSky)" />

    {/* Pixel Stars */}
    <g fill="#e2e8f0" opacity="0.65">
      <rect x="75" y="26" width="4" height="4" />
      <rect x="210" y="42" width="4" height="4" />
      <rect x="335" y="18" width="4" height="4" />
      <rect x="440" y="36" width="4" height="4" />
      <rect x="760" y="24" width="4" height="4" />
      <rect x="895" y="44" width="4" height="4" />
      <rect x="1040" y="20" width="4" height="4" />
      <rect x="1135" y="52" width="4" height="4" />
    </g>

    {/* Blocky Pixel Moon / Twilight Sun */}
    <g transform="translate(1015, 24)">
      <rect x="-10" y="-10" width="64" height="64" fill="#facc15" opacity="0.14" />
      <rect x="0" y="0" width="44" height="44" fill="#facc15" />
      <rect x="6" y="6" width="32" height="32" fill="#fef08a" />
      <rect x="10" y="10" width="8" height="8" fill="#eab308" opacity="0.35" />
      <rect x="24" y="22" width="10" height="10" fill="#eab308" opacity="0.3" />
    </g>

    {/* Blocky Clouds */}
    <g fill="#cbd5e1" opacity="0.2">
      <rect x="100" y="34" width="104" height="16" />
      <rect x="128" y="22" width="52" height="12" />
      <rect x="360" y="48" width="96" height="14" />
      <rect x="780" y="32" width="112" height="16" />
      <rect x="812" y="20" width="56" height="12" />
    </g>

    {/* Ancient Stone Ruins Silhouettes (Background) */}
    <g fill="#1b2230">
      {/* Left Broken Ruin Pillar */}
      <rect x="42" y="104" width="32" height="86" />
      <rect x="36" y="96" width="44" height="10" />
      <rect x="84" y="138" width="28" height="52" />
      {/* Distant Deepslate Hills */}
      <rect x="240" y="128" width="150" height="62" />
      <rect x="276" y="106" width="76" height="22" />
      <rect x="790" y="122" width="170" height="68" />
      <rect x="835" y="98" width="84" height="24" />
      {/* Right Ruined Arch */}
      <rect x="1070" y="102" width="24" height="88" />
      <rect x="1136" y="114" width="24" height="76" />
      <rect x="1064" y="94" width="66" height="12" />
    </g>

    {/* Voxel Oak Tree Left */}
    <g transform="translate(148, 82)">
      <rect x="26" y="54" width="20" height="54" fill="#713f12" />
      <rect x="34" y="54" width="6" height="54" fill="#854d0e" />
      <rect x="0" y="18" width="72" height="40" fill="#15803d" />
      <rect x="12" y="4" width="48" height="18" fill="#16a34a" />
      <rect x="10" y="26" width="16" height="12" fill="#22c55e" />
      <rect x="44" y="20" width="16" height="12" fill="#22c55e" />
      <rect x="26" y="42" width="18" height="12" fill="#14532d" />
    </g>

    {/* Creeper Silhouette Standing Near Ruins */}
    <g transform="translate(316, 114)">
      <rect x="6" y="0" width="28" height="28" fill="#22c55e" />
      <rect x="6" y="0" width="28" height="6" fill="#4ade80" opacity="0.45" />
      <rect x="11" y="7" width="6" height="6" fill="#090b10" />
      <rect x="23" y="7" width="6" height="6" fill="#090b10" />
      <rect x="17" y="13" width="6" height="8" fill="#090b10" />
      <rect x="13" y="17" width="4" height="8" fill="#090b10" />
      <rect x="23" y="17" width="4" height="8" fill="#090b10" />
      <rect x="10" y="28" width="20" height="32" fill="#16a34a" />
      <rect x="6" y="60" width="12" height="16" fill="#15803d" />
      <rect x="22" y="60" width="12" height="16" fill="#15803d" />
    </g>

    {/* CENTERPIECE: OBSIDIAN TIME PORTAL / PAST SIMPLE */}
    <g transform="translate(500, 28)">
      <circle cx="100" cy="88" r="120" fill="url(#portalGlow)" />
      {/* Inner Swirling Portal */}
      <rect x="24" y="24" width="152" height="136" fill="url(#portalSwirl)" />
      {/* Pixel Portal Shimmer Squares */}
      <g fill="#e0f2fe" opacity="0.35">
        <rect x="38" y="42" width="14" height="14" />
        <rect x="140" y="54" width="16" height="16" />
        <rect x="52" y="114" width="18" height="12" />
        <rect x="128" y="120" width="14" height="14" />
      </g>
      <g fill="#f0abfc" opacity="0.35">
        <rect x="74" y="34" width="12" height="12" />
        <rect x="108" y="128" width="16" height="10" />
      </g>

      {/* Obsidian Block Frame */}
      <g fill="#1c1926" stroke="#3b2f5c" strokeWidth="1.5">
        {/* Top Beam */}
        <rect x="4" y="4" width="192" height="22" />
        {/* Left Pillar */}
        <rect x="4" y="26" width="22" height="136" />
        {/* Right Pillar */}
        <rect x="174" y="26" width="22" height="136" />
        {/* Cracked Gold / Ruined Portal Accents */}
        <rect x="4" y="4" width="22" height="22" fill="#2e1065" />
        <rect x="174" y="4" width="22" height="22" fill="#2e1065" />
        <rect x="86" y="4" width="28" height="22" fill="#ca8a04" stroke="#facc15" />
      </g>

      {/* Portal Text Banner */}
      <rect x="32" y="64" width="136" height="46" rx="3" fill="#090b10" opacity="0.72" />
      <text
        x="100"
        y="83"
        textAnchor="middle"
        fill="#38bdf8"
        fontSize="11"
        fontWeight="700"
        fontFamily="monospace"
        letterSpacing="1.5"
      >
        TIME PORTAL
      </text>
      <text
        x="100"
        y="101"
        textAnchor="middle"
        fill="#facc15"
        fontSize="13"
        fontWeight="700"
        fontFamily="monospace"
        letterSpacing="1"
      >
        PAST SIMPLE
      </text>
    </g>

    {/* Floating Glowing Diamond Pickaxe Right */}
    <g transform="translate(808, 56) scale(1.12)">
      <circle cx="44" cy="24" r="34" fill="#38bdf8" opacity="0.14" />
      {/* Wooden Handle */}
      <rect x="12" y="56" width="8" height="8" fill="#78350f" />
      <rect x="20" y="48" width="8" height="8" fill="#92400e" />
      <rect x="28" y="40" width="8" height="8" fill="#78350f" />
      <rect x="36" y="32" width="8" height="8" fill="#92400e" />
      <rect x="44" y="24" width="8" height="8" fill="#78350f" />
      {/* Diamond Head */}
      <rect x="20" y="8" width="8" height="8" fill="#0284c7" />
      <rect x="28" y="8" width="16" height="8" fill="#7dd3fc" />
      <rect x="44" y="8" width="8" height="8" fill="#38bdf8" />
      <rect x="52" y="16" width="8" height="8" fill="#bae6fd" />
      <rect x="52" y="24" width="8" height="16" fill="#38bdf8" />
      <rect x="52" y="40" width="8" height="8" fill="#0284c7" />
      <rect x="44" y="16" width="8" height="8" fill="#e0f2fe" />
    </g>

    {/* Voxel Oak Tree Far Right */}
    <g transform="translate(940, 92)">
      <rect x="22" y="46" width="18" height="52" fill="#713f12" />
      <rect x="0" y="16" width="62" height="34" fill="#15803d" />
      <rect x="12" y="4" width="38" height="14" fill="#16a34a" />
      <rect x="12" y="22" width="14" height="10" fill="#22c55e" />
    </g>

    {/* Foreground Grass & Dirt Layer */}
    <g>
      <rect x="0" y="190" width="1200" height="12" fill="#22c55e" />
      <rect x="0" y="202" width="1200" height="28" fill="#57341a" />
      {Array.from({ length: 24 }).map((_, i) => (
        <g key={i}>
          <rect x={i * 50 + 6} y="202" width="14" height="5" fill="#16a34a" />
          <rect x={i * 50 + 28} y="202" width="8" height="4" fill="#15803d" />
          <rect x={i * 50 + 16} y="212" width="8" height="6" fill="#452712" />
          <rect x={i * 50 + 38} y="216" width="6" height="6" fill="#6b4226" />
        </g>
      ))}
    </g>
  </svg>
);

/**
 * Custom Pixel-Style Inline SVG Icons for Categories, Pickaxe Ranks & Tools
 */
const PixelIconSVG = ({ type, className = 'w-10 h-10' }) => {
  switch (type) {
    case 'wood-plank':
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#78350f" />
          <rect x="2" y="2" width="28" height="7" fill="#b45309" />
          <rect x="2" y="11" width="28" height="7" fill="#a16207" />
          <rect x="2" y="20" width="28" height="10" fill="#92400e" />
          <rect x="14" y="2" width="2" height="7" fill="#713f12" />
          <rect x="22" y="11" width="2" height="7" fill="#713f12" />
          <rect x="9" y="20" width="2" height="10" fill="#713f12" />
        </svg>
      );
    case 'anvil':
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#181c24" />
          <rect x="4" y="7" width="24" height="7" fill="#64748b" />
          <rect x="6" y="7" width="20" height="3" fill="#94a3b8" />
          <rect x="11" y="14" width="10" height="6" fill="#475569" />
          <rect x="6" y="20" width="20" height="6" fill="#334155" />
          <rect x="8" y="20" width="16" height="2" fill="#64748b" />
        </svg>
      );
    case 'redstone-torch':
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#1f1621" />
          <rect x="13" y="14" width="6" height="14" fill="#92400e" />
          <rect x="14" y="14" width="2" height="14" fill="#b45309" />
          <rect x="9" y="4" width="14" height="11" fill="#ef4444" opacity="0.35" />
          <rect x="12" y="7" width="8" height="7" fill="#ef4444" />
          <rect x="14" y="9" width="4" height="3" fill="#fef08a" />
        </svg>
      );
    case 'shield':
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#111827" />
          <rect x="6" y="4" width="20" height="24" fill="#94a3b8" />
          <rect x="9" y="7" width="14" height="18" fill="#78350f" />
          <rect x="13" y="10" width="6" height="12" fill="#38bdf8" />
          <rect x="15" y="12" width="2" height="8" fill="#e0f2fe" />
        </svg>
      );
    case 'creeper':
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#15803d" />
          <rect x="2" y="2" width="28" height="28" rx="2" fill="#22c55e" />
          <rect x="6" y="8" width="6" height="6" fill="#090b10" />
          <rect x="20" y="8" width="6" height="6" fill="#090b10" />
          <rect x="12" y="14" width="8" height="8" fill="#090b10" />
          <rect x="9" y="18" width="4" height="8" fill="#090b10" />
          <rect x="19" y="18" width="4" height="8" fill="#090b10" />
        </svg>
      );
    case 'clock':
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#1b1f27" />
          <rect x="6" y="4" width="20" height="24" rx="4" fill="#eab308" />
          <rect x="4" y="6" width="24" height="20" rx="4" fill="#facc15" />
          <rect x="8" y="8" width="16" height="16" rx="2" fill="#1e293b" />
          <rect x="8" y="8" width="16" height="8" fill="#38bdf8" />
          <rect x="14" y="10" width="4" height="4" fill="#fef08a" />
          <rect x="15" y="14" width="2" height="8" fill="#ef4444" />
        </svg>
      );
    case 'enchanted-book':
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#1e1b4b" />
          <rect x="6" y="5" width="20" height="22" fill="#7e22ce" />
          <rect x="9" y="7" width="15" height="18" fill="#a855f7" />
          <rect x="6" y="5" width="4" height="22" fill="#facc15" />
          <rect x="14" y="12" width="6" height="3" fill="#fef08a" />
          <rect x="14" y="17" width="8" height="2" fill="#e9d5ff" />
        </svg>
      );
    case 'pickaxe-wood':
    case 'pickaxe-stone':
    case 'pickaxe-iron':
    case 'pickaxe-diamond':
    case 'pickaxe-netherite': {
      const palette = {
        'pickaxe-wood': { main: '#a16207', light: '#ca8a04', dark: '#713f12' },
        'pickaxe-stone': { main: '#94a3b8', light: '#cbd5e1', dark: '#475569' },
        'pickaxe-iron': { main: '#e2e8f0', light: '#ffffff', dark: '#94a3b8' },
        'pickaxe-diamond': { main: '#38bdf8', light: '#7dd3fc', dark: '#0284c7' },
        'pickaxe-netherite': { main: '#57534e', light: '#c084fc', dark: '#292524' }
      }[type];
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#111318" />
          <rect x="6" y="22" width="4" height="4" fill="#78350f" />
          <rect x="10" y="18" width="4" height="4" fill="#92400e" />
          <rect x="14" y="14" width="4" height="4" fill="#78350f" />
          <rect x="18" y="10" width="4" height="4" fill="#92400e" />
          <rect x="10" y="4" width="4" height="4" fill={palette.dark} />
          <rect x="14" y="4" width="8" height="4" fill={palette.light} />
          <rect x="22" y="4" width="4" height="4" fill={palette.main} />
          <rect x="22" y="8" width="4" height="4" fill={palette.light} />
          <rect x="24" y="12" width="4" height="6" fill={palette.main} />
          <rect x="24" y="18" width="4" height="4" fill={palette.dark} />
        </svg>
      );
    }
    default:
      return (
        <svg viewBox="0 0 32 32" className={className} aria-hidden="true">
          <rect width="32" height="32" rx="3" fill="#22c55e" />
        </svg>
      );
  }
};

// ============================================================================
// 2. QUIZ DATA: EXACTLY 50 UNIQUE A2-B1 PAST SIMPLE QUESTIONS
// 5 Categories × 10 Questions (7 'fill' + 3 'four_sentences' each) = 35 fill + 15 four_sentences
// ============================================================================

const QUIZ_QUESTIONS = [
  // ==========================================================================
  // CATEGORY 1: REGULAR VERBS & -ED SPELLING (10 questions: 7 fill, 3 four_sentences)
  // ==========================================================================
  {
    id: 1,
    type: 'fill',
    category: 'regular',
    prompt: 'Yesterday afternoon, I _____ forty blocks of coal in a huge cave.',
    germanHint: 'Gestern Nachmittag baute ich vierzig Blöcke Kohle in einer riesigen Höhle ab. (mine)',
    options: ['mined', 'mineed', 'mound', 'mining'],
    correctIndex: 0,
    explanation: 'Bei regelmäßigen Verben, die schon auf „-e“ enden (mine → mined), hängt man einfach nur ein „-d“ an.'
  },
  {
    id: 2,
    type: 'fill',
    category: 'regular',
    prompt: 'After school, Leon _____ a full set of iron armour before entering the Nether.',
    germanHint: 'Nach der Schule craftete Leon eine komplette Eisenrüstung. (craft)',
    options: ['craftet', 'crafted', 'craft', 'croft'],
    correctIndex: 1,
    explanation: '„Craft“ ist ein normales regelmäßiges Verb: einfach „-ed“ anhängen → crafted.'
  },
  {
    id: 3,
    type: 'fill',
    category: 'regular',
    prompt: 'I _____ to jump across the lava river, and I barely made it!',
    germanHint: 'Ich versuchte, über den Lavafluss zu springen, und schaffte es gerade so! (try)',
    options: ['tryed', 'tryd', 'tried', 'trying'],
    correctIndex: 2,
    explanation: 'Rechtschreib-Regel: Endet ein Verb auf Konsonant + y (try), wird das „y“ zu „ied“ → tried.'
  },
  {
    id: 4,
    type: 'fill',
    category: 'regular',
    prompt: 'Suddenly, the noisy zombie _____ right in front of our oak door.',
    germanHint: 'Plötzlich blieb der laute Zombie direkt vor unserer Eichentür stehen. (stop)',
    options: ['stoped', 'stoppt', 'stopped', 'stoping'],
    correctIndex: 2,
    explanation: 'Bei kurzen Verben mit kurzem Vokal + einfachem Konsonanten am Ende (stop) wird der letzte Konsonant verdoppelt → stopped.'
  },
  {
    id: 5,
    type: 'fill',
    category: 'regular',
    prompt: 'Last Saturday, my best friend and I _____ BedWars for two hours.',
    germanHint: 'Letzten Samstag spielten mein bester Freund und ich zwei Stunden lang BedWars. (play)',
    options: ['plaied', 'played', 'playd', 'plaid'],
    correctIndex: 1,
    explanation: 'Achtung! Steht vor dem „y“ ein Vokal (a, e, o, u wie in „play“), bleibt das „y“ einfach stehen → played (NICHT plaied!).'
  },
  {
    id: 6,
    type: 'fill',
    category: 'regular',
    prompt: 'Oops! I accidentally _____ my enchanted diamond sword into the cactus!',
    germanHint: 'Ups! Ich ließ mein verzaubertes Diamantschwert versehentlich in den Kaktus fallen! (drop)',
    options: ['droped', 'dropped', 'dropt', 'droppd'],
    correctIndex: 1,
    explanation: '„Drop“ ist kurz und endet auf Vokal + Konsonant (o + p) → das „p“ wird verdoppelt: dropped.'
  },
  {
    id: 7,
    type: 'fill',
    category: 'regular',
    prompt: 'Before gaming on Friday, Max _____ his English vocabulary for 30 minutes.',
    germanHint: 'Vor dem Zocken am Freitag lernte Max 30 Minuten lang seine Englischvokabeln. (study)',
    options: ['studyed', 'studid', 'studied', 'studying'],
    correctIndex: 2,
    explanation: 'Bei „study“ steht ein Konsonant (d) vor dem „y“ → aus „y“ wird „ied“: studied.'
  },
  {
    id: 8,
    type: 'four_sentences',
    category: 'regular',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: -ed-Rechtschreibung mit „carry“)',
    germanHint: 'Sinn: Wir trugen zwei volle Shulker-Boxen zurück zu unserer Base.',
    options: [
      'We carryed two full Shulker boxes back to our base.',
      'We carried two full Shulker boxes back to our base.',
      'We carred two full Shulker boxes back to our base.',
      'We carryd two full Shulker boxes back to our base.'
    ],
    correctIndex: 1,
    explanation: 'Bei „carry“ steht der Konsonant „r“ vor dem „y“, deshalb wird das „y“ zu „i“ + „-ed“ → carried.'
  },
  {
    id: 9,
    type: 'four_sentences',
    category: 'regular',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: Verdopplung bei „plan“)',
    germanHint: 'Sinn: Unsere Klasse plante letzte Woche eine riesige Mittelalterstadt auf dem Server.',
    options: [
      'Our class planed a huge medieval city on the server last week.',
      'Our class plannd a huge medieval city on the server last week.',
      'Our class planned a huge medieval city on the server last week.',
      'Our class planning a huge medieval city on the server last week.'
    ],
    correctIndex: 2,
    explanation: '„Plan“ hat einen kurzen betonten Vokal vor einem einzelnen Konsonanten → das „n“ wird verdoppelt: planned („planed“ wäre „hobelte“).'
  },
  {
    id: 10,
    type: 'four_sentences',
    category: 'regular',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: „visit“ & „stay“)',
    germanHint: 'Sinn: Wir besuchten das Wüstendorf und blieben bis zum Sonnenaufgang.',
    options: [
      'We visitted the desert village and staied until sunrise.',
      'We visited the desert village and stayed until sunrise.',
      'We visited the desert village and stayd until sunrise.',
      'We visit the desert village and stayed until sunrise.'
    ],
    correctIndex: 1,
    explanation: '„Visit“ wird auf der ersten Silbe betont (kein Doppel-t → visited) und bei „stay“ steht ein Vokal vor dem „y“ (→ stayed).'
  },

  // ==========================================================================
  // CATEGORY 2: IRREGULAR VERBS (10 questions: 7 fill, 3 four_sentences)
  // ==========================================================================
  {
    id: 11,
    type: 'fill',
    category: 'irregular',
    prompt: 'Last weekend, my friends and I _____ an underground Redstone bunker.',
    germanHint: 'Letztes Wochenende bauten meine Freunde und ich einen unterirdischen Redstone-Bunker. (build)',
    options: ['builded', 'built', 'bild', 'building'],
    correctIndex: 1,
    explanation: '„Build“ ist unregelmäßig: build – built – built. Niemals „builded“!'
  },
  {
    id: 12,
    type: 'fill',
    category: 'irregular',
    prompt: 'Tim _____ a staircase all the way down to level -58 to look for diamonds.',
    germanHint: 'Tim grub eine Treppe ganz hinunter bis Höhe -58, um Diamanten zu suchen. (dig)',
    options: ['digged', 'dag', 'dug', 'dog'],
    correctIndex: 2,
    explanation: 'Die 2. Form von „dig“ (graben) ist „dug“ (dig – dug – dug).'
  },
  {
    id: 13,
    type: 'fill',
    category: 'irregular',
    prompt: 'Guess what! I _____ a chest with two enchanted golden apples in the ancient city!',
    germanHint: 'Rate mal! Ich fand eine Truhe mit zwei verzauberten goldenen Äpfeln! (find)',
    options: ['finded', 'fand', 'found', 'founded'],
    correctIndex: 2,
    explanation: '„Find“ wird im Past Simple zu „found“ (find – found – found). „Founded“ bedeutet „gründete“ (z. B. eine Firma).'
  },
  {
    id: 14,
    type: 'fill',
    category: 'irregular',
    prompt: 'We _____ through the purple portal and landed right next to a Bastion.',
    germanHint: 'Wir gingen durch das lila Portal und landeten direkt neben einer Bastion. (go)',
    options: ['goed', 'went', 'gone', 'going'],
    correctIndex: 1,
    explanation: 'Eines der wichtigsten unregelmäßigen Verben: go – went – gone. Im Past Simple immer „went“!'
  },
  {
    id: 15,
    type: 'fill',
    category: 'irregular',
    prompt: 'Together, our squad _____ the Ender Dragon and saved the End island.',
    germanHint: 'Zusammen bekämpfte unser Squad den Enderdrachen und rettete die End-Insel. (fight)',
    options: ['fighted', 'faught', 'fought', 'fight'],
    correctIndex: 2,
    explanation: '„Fight“ hat die unregelmäßige 2. Form „fought“ (mit „ou“, genau wie bought und thought).'
  },
  {
    id: 16,
    type: 'fill',
    category: 'irregular',
    prompt: 'Oh no! My iron pickaxe _____ just when I reached the obsidian wall.',
    germanHint: 'Oh nein! Meine Eisenspitzhacke zerbrach genau dann, als ich die Obsidianwand erreichte. (break)',
    options: ['breaked', 'broken', 'broke', 'brake'],
    correctIndex: 2,
    explanation: 'break – broke – broken. Für das Past Simple brauchst du die 2. Form: „broke“.'
  },
  {
    id: 17,
    type: 'fill',
    category: 'irregular',
    prompt: 'At the village market, Jonas _____ a Mending book from the librarian for 14 emeralds.',
    germanHint: 'Auf dem Dorfmarkt kaufte Jonas ein Reparatur-Buch für 14 Smaragde. (buy)',
    options: ['buyed', 'bought', 'brought', 'baught'],
    correctIndex: 1,
    explanation: 'buy – bought – bought (kaufen). Nicht verwechseln mit „brought“ (= brachte, von bring)!'
  },
  {
    id: 18,
    type: 'four_sentences',
    category: 'irregular',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: „fall“ & „lose“)',
    germanHint: 'Sinn: Ich fiel in eine tiefe Schlucht und verlor alle meine Fackeln.',
    options: [
      'I falled into a deep ravine and losed all my torches.',
      'I fell into a deep ravine and lost all my torches.',
      'I fallen into a deep ravine and lost all my torches.',
      'I felt into a deep ravine and lose all my torches.'
    ],
    correctIndex: 1,
    explanation: 'fall – fell – fallen (fiel) und lose – lost – lost (verlor). „Felt“ kommt von „feel“ (fühlen), nicht von „fall“!'
  },
  {
    id: 19,
    type: 'four_sentences',
    category: 'irregular',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: „see“ & „swim“)',
    germanHint: 'Sinn: Wir sahen ein Ozeanmonument und schwammen schnell zur Oberfläche zurück.',
    options: [
      'We seed an ocean monument and swimmed back to the surface fast.',
      'We seen an ocean monument and swum back to the surface fast.',
      'We saw an ocean monument and swam back to the surface fast.',
      'We saw an ocean monument and swimmed back to the surface fast.'
    ],
    correctIndex: 2,
    explanation: 'Beide Verben sind unregelmäßig: see → saw (2. Form) und swim → swam (2. Form).'
  },
  {
    id: 20,
    type: 'four_sentences',
    category: 'irregular',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: „write“ & „win“)',
    germanHint: 'Sinn: Ben schrieb eine gute Englischarbeit und gewann abends das Minecraft-Turnier.',
    options: [
      'Ben writed a great English test and winned the Minecraft tournament in the evening.',
      'Ben written a great English test and won the Minecraft tournament in the evening.',
      'Ben wrote a great English test and winned the Minecraft tournament in the evening.',
      'Ben wrote a great English test and won the Minecraft tournament in the evening.'
    ],
    correctIndex: 3,
    explanation: 'write – wrote – written (schrieb) und win – won – won (gewann). Beide stehen in der 2. Form!'
  },

  // ==========================================================================
  // CATEGORY 3: NEGATIVES & QUESTIONS WITH DID / DIDN'T (10: 7 fill, 3 four_sentences)
  // ==========================================================================
  {
    id: 21,
    type: 'fill',
    category: 'neg_quest',
    prompt: 'I _____ into the Deep Dark cave because I didn’t have any wool blocks.',
    germanHint: 'Ich ging nicht in die Deep-Dark-Höhle, weil ich keine Wollblöcke hatte. (not go)',
    options: ["didn't went", "didn't go", "wasn't go", "don't went"],
    correctIndex: 1,
    explanation: 'Goldene Regel: Nach „didn’t“ steht IMMER die Grundform (Infinitiv) des Verbs → didn’t go (NIEMALS didn’t went!).'
  },
  {
    id: 22,
    type: 'fill',
    category: 'neg_quest',
    prompt: '_____ you _____ any Netherite scraps during your mining trip yesterday?',
    germanHint: 'Hast du gestern bei deiner Mining-Tour Netheritschrott gefunden? (find)',
    options: ['Did / found', 'Were / find', 'Did / find', 'Do / found'],
    correctIndex: 2,
    explanation: 'Fragen im Past Simple bildet man mit „Did + Subjekt + Grundform“ → Did you find...?'
  },
  {
    id: 23,
    type: 'fill',
    category: 'neg_quest',
    prompt: 'What _____ Steve _____ with all that Redstone dust?',
    germanHint: 'Was hat Steve mit all dem Redstone-Staub gebaut? (build)',
    options: ['did / built', 'did / build', 'was / build', 'does / built'],
    correctIndex: 1,
    explanation: 'Auch bei W-Fragen (What / Where / Why) gilt: „did“ trägt schon die Vergangenheit, das Verb bleibt in der Grundform → What did Steve build?'
  },
  {
    id: 24,
    type: 'fill',
    category: 'neg_quest',
    prompt: '“Did your brother defeat the Wither alone?” — “No, he _____.”',
    germanHint: 'Kurzantwort auf Englisch: „Nein, das hat er nicht.“',
    options: ["wasn't", "didn't", "don't", "didn't defeated"],
    correctIndex: 1,
    explanation: 'Wenn die Frage mit „Did…?“ beginnt, antwortet man kurz mit „Yes, … did“ oder „No, … didn’t“.'
  },
  {
    id: 25,
    type: 'fill',
    category: 'neg_quest',
    prompt: 'Why _____ Lukas _____ a water bucket before jumping off the tower?',
    germanHint: 'Warum hat Lukas keinen Wassereimer mitgenommen, bevor er vom Turm sprang? (not take)',
    options: ["didn't / took", "wasn't / take", "didn't / take", "don't / take"],
    correctIndex: 2,
    explanation: 'Verneinte W-Frage im Past Simple: „Why didn’t + Subjekt + Grundform“ → Why didn’t Lukas take...?'
  },
  {
    id: 26,
    type: 'fill',
    category: 'neg_quest',
    prompt: 'The Creeper _____ our house because my wolf scared it away—wait, cats scare Creepers!',
    germanHint: 'Der Creeper hat unser Haus nicht zerstört! (not destroy)',
    options: ["didn't destroyed", "not destroyed", "didn't destroy", "wasn't destroy"],
    correctIndex: 2,
    explanation: 'Für die Verneinung normaler Verben im Past Simple brauchst du immer „didn’t“ + Grundform → didn’t destroy.'
  },
  {
    id: 27,
    type: 'fill',
    category: 'neg_quest',
    prompt: '“Did you and Mia finish your biology poster before gaming?” — “Yes, we _____!”',
    germanHint: 'Kurzantwort: „Ja, das haben wir!“',
    options: ['did', 'were', 'finished', 'do'],
    correctIndex: 0,
    explanation: 'Auf „Did you and Mia…?“ lautet die korrekte englische Kurzantwort einfach „Yes, we did!“ (ohne das Vollverb zu wiederholen).'
  },
  {
    id: 28,
    type: 'four_sentences',
    category: 'neg_quest',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: Verneinung mit „didn’t“)',
    germanHint: 'Sinn: Ich habe gestern Abend meine Hausaufgaben nicht vergessen.',
    options: [
      "I didn't forgot my homework last night.",
      "I not forgot my homework last night.",
      "I didn't forget my homework last night.",
      "I wasn't forget my homework last night."
    ],
    correctIndex: 2,
    explanation: 'Nach „didn’t“ schaltet das Verb zurück in die 1. Form (Grundform): „didn’t forget“ – niemals „didn’t forgot“!'
  },
  {
    id: 29,
    type: 'four_sentences',
    category: 'neg_quest',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: Fragen mit „Did“)',
    germanHint: 'Sinn: Wo hast du gestern diese coole Minecraft-Map heruntergeladen?',
    options: [
      'Where did you downloaded that cool Minecraft map yesterday?',
      'Where you downloaded that cool Minecraft map yesterday?',
      'Where did you download that cool Minecraft map yesterday?',
      'Where were you download that cool Minecraft map yesterday?'
    ],
    correctIndex: 2,
    explanation: 'Frageformel: Fragewort (Where) + did + Subjekt (you) + Grundform (download) → kein „-ed“ am Verb!'
  },
  {
    id: 30,
    type: 'four_sentences',
    category: 'neg_quest',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: „didn’t“ bei unregelmäßigen Verben)',
    germanHint: 'Sinn: Wir sahen keine Diamanten, deshalb bauten wir stattdessen Eisen ab.',
    options: [
      "We didn't saw any diamonds, so we mined iron instead.",
      "We didn't see any diamonds, so we mined iron instead.",
      "We didn't seen any diamonds, so we mined iron instead.",
      "We don't saw any diamonds, so we mined iron instead."
    ],
    correctIndex: 1,
    explanation: 'Im ersten Teil steht „didn’t + Grundform“ (didn’t see), im zweiten Teil eine normale positive Aussage im Past Simple (mined).'
  },

  // ==========================================================================
  // CATEGORY 4: WAS / WERE & COULD (10 questions: 7 fill, 3 four_sentences)
  // ==========================================================================
  {
    id: 31,
    type: 'fill',
    category: 'was_were',
    prompt: 'I _____ super nervous when I heard the Warden’s heartbeat in the dark.',
    germanHint: 'Ich war super nervös, als ich den Herzschlag des Wardens hörte. (be)',
    options: ['were', 'was', 'did be', 'am'],
    correctIndex: 1,
    explanation: 'Bei I / he / she / it verwendet man im Past Simple immer „was“.'
  },
  {
    id: 32,
    type: 'fill',
    category: 'was_were',
    prompt: 'My friends and I _____ at the top of the mountain base when the storm started.',
    germanHint: 'Meine Freunde und ich waren ganz oben in der Berg-Base, als der Sturm begann. (be)',
    options: ['was', 'were', 'did', 'are'],
    correctIndex: 1,
    explanation: '„My friends and I“ = we (Mehrzahl) → deshalb gehört hier „were“ hin!'
  },
  {
    id: 33,
    type: 'fill',
    category: 'was_were',
    prompt: '_____ you online on our school SMP server last night?',
    germanHint: 'Warst du gestern Abend auf unserem Schul-SMP-Server online?',
    options: ['Did', 'Was', 'Were', 'Are'],
    correctIndex: 2,
    explanation: 'Bei „you“ steht immer „were“ – und bei was/were benutzt man NIEMALS „did“!'
  },
  {
    id: 34,
    type: 'fill',
    category: 'was_were',
    prompt: 'Look at that screenshot! There _____ three baby pandas in the bamboo jungle.',
    germanHint: 'Es gab drei Baby-Pandas im Bambusdschungel. (There be)',
    options: ['was', 'were', 'had', 'did'],
    correctIndex: 1,
    explanation: '„Three baby pandas“ ist Plural (Mehrzahl) → „There were“ (es gab). Für Einzahl nimmt man „There was“.'
  },
  {
    id: 35,
    type: 'fill',
    category: 'was_were',
    prompt: 'The maths test _____ as hard as I feared, so I finished ten minutes early.',
    germanHint: 'Der Mathetest war nicht so schwer, wie ich befürchtet hatte. (not be)',
    options: ["didn't be", "weren't", "wasn't", "not was"],
    correctIndex: 2,
    explanation: '„The maths test“ = it → die Verneinung von „was“ ist einfach „wasn’t“ (ohne „didn’t“!).'
  },
  {
    id: 36,
    type: 'fill',
    category: 'was_were',
    prompt: 'Because of the Elytra wings, I _____ glide all the way across the huge ocean.',
    germanHint: 'Dank der Elytra-Flügel konnte ich über den ganzen riesigen Ozean gleiten. (can → Past Simple)',
    options: ['can', 'could', 'did can', 'was can'],
    correctIndex: 1,
    explanation: 'Die Vergangenheit von „can“ ist „could“ (konnte). Es braucht kein „did“ und bleibt für alle Personen gleich.'
  },
  {
    id: 37,
    type: 'fill',
    category: 'was_were',
    prompt: 'There _____ a hidden trapdoor right under the carpet in the woodland mansion!',
    germanHint: 'Es gab eine versteckte Falltür direkt unter dem Teppich in der Waldvilla!',
    options: ['were', 'was', 'did', 'are'],
    correctIndex: 1,
    explanation: '„A hidden trapdoor“ ist Singular (Einzahl) → deshalb „There was“.'
  },
  {
    id: 38,
    type: 'four_sentences',
    category: 'was_were',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: Frage mit „were“)',
    germanHint: 'Sinn: Wart ihr nach dem langen Bosskampf müde?',
    options: [
      'Did you were tired after the long boss fight?',
      'Was you tired after the long boss fight?',
      'Were you tired after the long boss fight?',
      'Did you be tired after the long boss fight?'
    ],
    correctIndex: 2,
    explanation: '„was“ und „were“ sind starke Verben: Sie brauchen KEIN „did“! Man tauscht einfach Subjekt und „were“ → Were you tired?'
  },
  {
    id: 39,
    type: 'four_sentences',
    category: 'was_were',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: „wasn’t / weren’t“)',
    germanHint: 'Sinn: Die Dorfbewohner waren nicht in ihren Häusern, weil es noch Tag war.',
    options: [
      "The villagers didn't be in their houses because it was still daytime.",
      "The villagers wasn't in their houses because it was still daytime.",
      "The villagers weren't in their houses because it was still daytime.",
      "The villagers not were in their houses because it was still daytime."
    ],
    correctIndex: 2,
    explanation: '„The villagers“ = they (Plural) → „weren’t“. Bei „be“ im Past Simple benutzt man niemals „didn’t“.'
  },
  {
    id: 40,
    type: 'four_sentences',
    category: 'was_were',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: „couldn’t“)',
    germanHint: 'Sinn: Ich konnte das Portal gestern Abend nicht anzünden, weil mir Feuerstein fehlte.',
    options: [
      "I didn't could light the portal last night because I had no flint.",
      "I couldn't lit the portal last night because I had no flint.",
      "I couldn't light the portal last night because I had no flint.",
      "I wasn't could light the portal last night because I had no flint."
    ],
    correctIndex: 2,
    explanation: '„Couldn’t“ braucht kein „did“ und steht immer mit der Grundform des Verbs („couldn’t light“).'
  },

  // ==========================================================================
  // CATEGORY 5: SIGNAL WORDS & GERMAN SPEAKER TRAPS (10: 7 fill, 3 four_sentences)
  // ==========================================================================
  {
    id: 41,
    type: 'fill',
    category: 'traps',
    prompt: 'I _____ a massive treehouse on our server yesterday.',
    germanHint: 'Achtung Deutsch-Falle! Im Deutschen sagt man „Ich habe gestern gebaut“, im Englischen steht bei „yesterday“ aber Past Simple!',
    options: ['have built', 'built', 'am building', 'have build'],
    correctIndex: 1,
    explanation: 'Die #1 Deutsch-Falle! Bei Signalwörtern wie „yesterday“ (abgeschlossene Vergangenheit) darf NIEMALS Present Perfect („have built“) stehen – immer Past Simple: „built“!'
  },
  {
    id: 42,
    type: 'fill',
    category: 'traps',
    prompt: 'Our class started this Minecraft world three months _____.',
    germanHint: 'Unsere Klasse startete diese Minecraft-Welt vor drei Monaten.',
    options: ['before', 'since', 'ago', 'last'],
    correctIndex: 2,
    explanation: '„Vor drei Monaten“ heißt auf Englisch „three months ago“ – und „ago“ steht immer AM ENDE der Zeitangabe (nicht davor wie „vor“ im Deutschen!).'
  },
  {
    id: 43,
    type: 'fill',
    category: 'traps',
    prompt: 'We _____ our first Nether fortress last night after dinner.',
    germanHint: 'Wir haben gestern Abend unsere erste Nether-Festung gefunden. (find)',
    options: ['have found', 'found', 'did found', 'finding'],
    correctIndex: 1,
    explanation: '„Last night“ ist ein klares Past-Simple-Signalwort! Deshalb „found“ statt „have found“.'
  },
  {
    id: 44,
    type: 'fill',
    category: 'traps',
    prompt: 'When I _____ ten years old, I built my very first dirt house.',
    germanHint: 'Als ich zehn Jahre alt war, baute ich mein allererstes Erdhaus.',
    options: ['have been', 'was', 'were', 'am'],
    correctIndex: 1,
    explanation: '„When I was ten years old“ beschreibt einen abgeschlossenen Zeitpunkt in der Vergangenheit → immer Past Simple („was“).'
  },
  {
    id: 45,
    type: 'fill',
    category: 'traps',
    prompt: 'Mojang _____ the Trial Chambers update in 2024.',
    germanHint: 'Mojang veröffentlichte das Trial-Chambers-Update im Jahr 2024. (release)',
    options: ['has released', 'released', 'was release', 'releasing'],
    correctIndex: 1,
    explanation: 'Bei vergangenen Jahreszahlen wie „in 2024“ steht im Englischen immer Past Simple → „released“ (kein Present Perfect!).'
  },
  {
    id: 46,
    type: 'fill',
    category: 'traps',
    prompt: '_____ week, our English teacher gave us a super fun gaming quiz.',
    germanHint: 'Letzte Woche gab uns unser Englischlehrer ein super cooles Gaming-Quiz.',
    options: ['Ago', 'Last', 'Yesterday', 'Before'],
    correctIndex: 1,
    explanation: '„Letzte Woche / letzten Monat / letztes Jahr“ heißt im Englischen „last week / last month / last year“ (ohne „the“!).'
  },
  {
    id: 47,
    type: 'fill',
    category: 'traps',
    prompt: '“When _____ you _____ playing Minecraft?” — “Two years ago!”',
    germanHint: 'Wann hast du angefangen, Minecraft zu spielen? (start)',
    options: ['have / started', 'did / start', 'did / started', 'were / start'],
    correctIndex: 1,
    explanation: 'Fragen mit „When…?“ fragen nach einem bestimmten Zeitpunkt in der Vergangenheit → IMMER Past Simple („When did you start…?“), niemals Present Perfect!'
  },
  {
    id: 48,
    type: 'four_sentences',
    category: 'traps',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: Perfekt-Falle mit „yesterday“)',
    germanHint: 'Sinn: Ich habe gestern zwei Stunden lang Minecraft gespielt.',
    options: [
      'I have played Minecraft for two hours yesterday.',
      'I played Minecraft for two hours yesterday.',
      'I did played Minecraft for two hours yesterday.',
      'Yesterday have I played Minecraft for two hours.'
    ],
    correctIndex: 1,
    explanation: 'Sobald „yesterday“ im Satz steht, ist „have played“ verboten! Und die englische Wortstellung lautet Subjekt – Verb – Objekt – Zeit.'
  },
  {
    id: 49,
    type: 'four_sentences',
    category: 'traps',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: Wortstellung mit „ago“)',
    germanHint: 'Sinn: Mein Freund hat vor zwei Tagen eine seltene rosa Schaf-Herde gesehen.',
    options: [
      'My friend has seen a rare pink sheep ago two days.',
      'My friend saw a rare pink sheep two days before.',
      'My friend saw a rare pink sheep two days ago.',
      'My friend saw ago two days a rare pink sheep.'
    ],
    correctIndex: 2,
    explanation: 'Zeitangaben mit „ago“ stehen am Satzende (oder ganz am Anfang) und „ago“ kommt NACH der Zeitspanne: „two days ago“ + Past Simple („saw“).'
  },
  {
    id: 50,
    type: 'four_sentences',
    category: 'traps',
    prompt: 'Welcher Satz im Past Simple ist grammatisch RICHTIG? (Fokus: Wortstellung bei Zeitangaben)',
    germanHint: 'Sinn: Wir haben gestern Abend im Survival-Modus eine neue Base gebaut.',
    options: [
      'We built last night in Survival mode a new base.',
      'We have built a new base in Survival mode last night.',
      'We built a new base in Survival mode last night.',
      'Last night built we a new base in Survival mode.'
    ],
    correctIndex: 2,
    explanation: 'Englische S-V-O-Regel: Subjekt (We) + Verb (built) + Objekt (a new base) + Ort (in Survival mode) + Zeit (last night). Keine Inversion wie im Deutschen („Gestern bauten wir“)!'
  }
];

// ============================================================================
// 3. CRAFTING-GUIDE: 12 DETAILED GRAMMAR RECIPE CARDS (5 SECTIONS EACH)
// ============================================================================

const GRAMMAR_RECIPES = [
  {
    id: 'reg-ed',
    category: 'regular',
    title: 'Regelmäßige Verben (-ed)',
    subtitle: 'mine → mined · craft → crafted',
    badge: 'Basis-Rezept',
    whenToUseDE:
      'Das Past Simple benutzt du für Handlungen, die in der Vergangenheit komplett abgeschlossen sind (z. B. gestern, letzte Woche, in den Ferien). Bei den meisten englischen Verben hängst du einfach „-ed“ an.',
    formula: 'Subjekt + Verb-Grundform + -ed  (für ALLE Personen gleich!)',
    formulaNoteDE:
      'Genial einfach: Im Past Simple gibt es KEIN „-s“ bei he/she/it! I played, he played, we played – überall dieselbe Form.',
    signalsDiffDE:
      'Typische Signalwörter: yesterday, last week, in 2024, two days ago. Wenn ein Verb auf „-e“ endet (mine, live, love), hängst du nur „-d“ an (mined, lived).',
    mistakesDE: [
      {
        wrong: 'He playeds Minecraft yesterday.',
        right: 'He played Minecraft yesterday.',
        note: 'Kein „-s“ bei he/she/it im Past Simple!'
      },
      {
        wrong: 'I mineed iron in the cave.',
        right: 'I mined iron in the cave.',
        note: 'Bei stummem „-e“ am Ende kommt nur ein „-d“ dazu.'
      }
    ],
    examples: [
      { en: 'I mined sixty blocks of iron yesterday.', de: 'Ich baute gestern sechzig Blöcke Eisen ab.' },
      { en: 'She crafted a new shield before the raid.', de: 'Sie craftete vor dem Raid einen neuen Schild.' }
    ]
  },
  {
    id: 'spelling-ed',
    category: 'regular',
    title: 'Rechtschreib-Regeln (-ed)',
    subtitle: 'try → tried · stop → stopped · play → played',
    badge: 'Rechtschreibung',
    whenToUseDE:
      'Bei manchen regelmäßigen Verben ändert sich die Schreibweise leicht, wenn „-ed“ angehängt wird. Diese 3 Regeln kommen in fast jeder Englisch-Klassenarbeit dran!',
    formula: 'Konsonant + y → -ied  |  Vokal + y → -yed  |  kurzer Vokal + Konsonant → Doppelkonsonant + -ed',
    formulaNoteDE:
      '1) try → tried, study → studied, carry → carried. 2) play → played, stay → stayed. 3) stop → stopped, drop → dropped, plan → planned.',
    signalsDiffDE:
      'Vorsicht bei zweisilbigen Verben wie „visit“ oder „open“: Weil die ERSTE Silbe betont wird, wird der letzte Buchstabe NICHT verdoppelt (visited, opened).',
    mistakesDE: [
      {
        wrong: 'I tryed to escape and droped my sword.',
        right: 'I tried to escape and dropped my sword.',
        note: 'Konsonant+y wird zu -ied; kurzes „drop“ verdoppelt das p!'
      },
      {
        wrong: 'We plaied BedWars all afternoon.',
        right: 'We played BedWars all afternoon.',
        note: 'Vor dem y steht ein Vokal (a) → das y bleibt stehen!'
      }
    ],
    examples: [
      { en: 'Max studied his English words, then played Minecraft.', de: 'Max lernte seine Englischwörter und spielte dann Minecraft.' },
      { en: 'The skeleton stopped right outside our wall.', de: 'Das Skelett blieb direkt vor unserer Mauer stehen.' }
    ]
  },
  {
    id: 'irregular-v2',
    category: 'irregular',
    title: 'Unregelmäßige Verben (2. Form)',
    subtitle: 'build → built · go → went · find → found',
    badge: 'Amboss-Wissen',
    whenToUseDE:
      'Viele der häufigsten englischen Verben (gehen, bauen, finden, kämpfen, sehen) halten sich nicht an die „-ed“-Regel. Sie haben eine eigene 2. Verbform, die man auswendig lernen muss.',
    formula: 'Subjekt + 2. Verbform (Past Simple)  — z. B. go → went, dig → dug',
    formulaNoteDE:
      'Wichtig: Die 2. Form benutzt du NUR in positiven Aussagesätzen! Sobald „did“ oder „didn’t“ ins Spiel kommt, springt das Verb zurück in die 1. Form.',
    signalsDiffDE:
      'Verwechsle die 2. Form (Past Simple: broke, saw, went) nicht mit der 3. Form (Past Participle: broken, seen, gone). Die 3. Form braucht man erst für Present Perfect oder Passiv.',
    mistakesDE: [
      {
        wrong: 'We builded a giant castle and finded diamonds.',
        right: 'We built a giant castle and found diamonds.',
        note: 'Niemals „-ed“ an unregelmäßige Verben anhängen!'
      },
      {
        wrong: 'I seen a Creeper behind the tree.',
        right: 'I saw a Creeper behind the tree.',
        note: '„seen“ ist die 3. Form – im Past Simple immer die 2. Form „saw“!'
      }
    ],
    examples: [
      { en: 'We dug down to level -58 and found eight diamonds.', de: 'Wir gruben bis Höhe -58 und fanden acht Diamanten.' },
      { en: 'Leo fought the Ender Dragon and won the game.', de: 'Leo kämpfte gegen den Enderdrachen und gewann das Spiel.' }
    ]
  },
  {
    id: 'neg-didnt',
    category: 'neg_quest',
    title: "Verneinung mit didn't",
    subtitle: "didn't go · didn't mine · didn't find",
    badge: 'Wichtigste Regel!',
    whenToUseDE:
      'Wenn du sagen willst, dass etwas in der Vergangenheit NICHT passiert ist, brauchst du bei allen normalen Verben (außer be & could) das Hilfsverb „didn’t“ (= did not).',
    formula: "Subjekt + didn't + Grundform (1. Form des Verbs)",
    formulaNoteDE:
      'Merkspruch: „Did hat die Vergangenheit schon im Inventar!“ Deshalb bleibt das Hauptverb danach IMMER in der Grundform (ohne -ed und ohne 2. Form).',
    signalsDiffDE:
      'Gilt für regelmäßige UND unregelmäßige Verben gleich: „didn’t play“, „didn’t go“, „didn’t build“. Einzige Ausnahmen: was/were (→ wasn’t/weren’t) und could (→ couldn’t).',
    mistakesDE: [
      {
        wrong: "I didn't went to the Nether yesterday.",
        right: "I didn't go to the Nether yesterday.",
        note: 'Der häufigste Klassenarbeits-Fehler überhaupt: Nach „didn’t“ nie die 2. Form!'
      },
      {
        wrong: "He not crafted a pickaxe.",
        right: "He didn't craft a pickaxe.",
        note: 'Im Englischen kann „not“ nie alleine vor dem Vollverb stehen.'
      }
    ],
    examples: [
      { en: "I didn't lose my sword because I kept it in my Ender Chest.", de: 'Ich habe mein Schwert nicht verloren, weil ich es in meiner Endertruhe aufbewahrte.' },
      { en: "We didn't finish the roof before sunset.", de: 'Wir wurden vor Sonnenuntergang nicht mit dem Dach fertig.' }
    ]
  },
  {
    id: 'yes-no-did',
    category: 'neg_quest',
    title: 'Entscheidungsfragen (Did you...?)',
    subtitle: 'Did you find...? · Did he build...?',
    badge: 'Ja/Nein-Fragen',
    whenToUseDE:
      'Um eine Ja/Nein-Frage über die Vergangenheit zu stellen („Hast du…?“ / „Bautest du…?“), stellst du einfach „Did“ ganz an den Satzanfang.',
    formula: 'Did + Subjekt + Grundform (1. Form) + ...?',
    formulaNoteDE:
      'Auch hier klaut „Did“ dem Verb die Vergangenheitsendung! Also „Did you mine?“ (NICHT „Did you mined?“).',
    signalsDiffDE:
      'Im Deutschen fragt man oft mit „Hast du gestern gespielt?“ – im Englischen übersetzt man das bei abgeschlossener Vergangenheit aber mit „Did you play yesterday?“!',
    mistakesDE: [
      {
        wrong: 'Did you found the village?',
        right: 'Did you find the village?',
        note: 'Nach „Did“ steht immer die Grundform „find“!'
      },
      {
        wrong: 'Played you Minecraft last night?',
        right: 'Did you play Minecraft last night?',
        note: 'Im Englischen tauscht man Vollverben nicht einfach nach vorne – man braucht „Did“.'
      }
    ],
    examples: [
      { en: 'Did you bring enough torches for the cave?', de: 'Hast du genug Fackeln für die Höhle mitgebracht?' },
      { en: 'Did Tom finish his maths homework before Discord?', de: 'Hat Tom seine Mathe-Hausaufgaben vor Discord fertig gemacht?' }
    ]
  },
  {
    id: 'wh-questions',
    category: 'neg_quest',
    title: 'W-Fragen (What / Where / Why did...?)',
    subtitle: 'What did you craft? · Where did they go?',
    badge: 'W-Fragen',
    whenToUseDE:
      'Wenn du genauere Infos wissen willst (Was? Wo? Wann? Warum? Wie?), setzt du einfach das englische Fragewort direkt vor „did“.',
    formula: 'Fragewort (What/Where/When/Why/How) + did + Subjekt + Grundform?',
    formulaNoteDE:
      'Achtung bei „Who“ als Subjektfrage („Wer hat das gebaut?“): Da fällt „did“ weg → „Who built this castle?“ (2. Form!).',
    signalsDiffDE:
      'Fragen mit „When…?“ stehen im Englischen fast immer im Past Simple („When did you start?“), weil nach einem festen Zeitpunkt gefragt wird.',
    mistakesDE: [
      {
        wrong: 'Where did you went after school?',
        right: 'Where did you go after school?',
        note: 'Grundform „go“ nach „did“!'
      },
      {
        wrong: 'What you built yesterday?',
        right: 'What did you build yesterday?',
        note: 'Vergiss das Hilfsverb „did“ nicht!'
      }
    ],
    examples: [
      { en: 'Where did you hide the diamond chest?', de: 'Wo hast du die Diamanttruhe versteckt?' },
      { en: 'Why did the Creeper explode near our farm?', de: 'Warum ist der Creeper in der Nähe unserer Farm explodiert?' }
    ]
  },
  {
    id: 'short-answers',
    category: 'neg_quest',
    title: 'Kurzantworten (Yes, I did)',
    subtitle: 'Yes, I did. · No, we didn’t.',
    badge: 'Höflich & Korrekt',
    whenToUseDE:
      'Im Englischen klingt ein einzelnes „Yes.“ oder „No.“ oft zu knapp oder unhöflich. Deshalb hängt man bei Ja/Nein-Fragen das Pronomen + Hilfsverb an.',
    formula: "Yes, + Pronomen + did.  |  No, + Pronomen + didn't.",
    formulaNoteDE:
      'Bei Fragen mit „Was/Were…?“ antwortet man natürlich mit was/were („Yes, I was.“ / „No, they weren’t.“), nicht mit did!',
    signalsDiffDE:
      'In Kurzantworten wiederholt man NIEMALS das Vollverb (also NICHT „Yes, I did played“).',
    mistakesDE: [
      {
        wrong: '“Did you win?” — “Yes, I wonned / Yes, I did win.”',
        right: '“Did you win?” — “Yes, I did!”',
        note: 'Kurz, knackig und perfekt: einfach „Yes, I did.“'
      },
      {
        wrong: '“Were you scared?” — “No, I didn’t.”',
        right: '“Were you scared?” — “No, I wasn’t.”',
        note: 'Das Hilfsverb in der Antwort passt immer zur Frage!'
      }
    ],
    examples: [
      { en: '“Did you beat the Ender Dragon?” — “Yes, we did!”', de: '„Habt ihr den Enderdrachen besiegt?“ — „Ja, haben wir!“' },
      { en: '“Did Mia lose her horse?” — “No, she didn’t.”', de: '„Hat Mia ihr Pferd verloren?“ — „Nein, hat sie nicht.“' }
    ]
  },
  {
    id: 'was-were-pos',
    category: 'was_were',
    title: 'was & were (Aussage)',
    subtitle: 'I / he / she / it was · you / we / they were',
    badge: 'Verb „to be“',
    whenToUseDE:
      '„was“ und „were“ sind die Vergangenheitsformen von „be“ (sein → war / waren). Damit beschreibst du Zustände, Gefühle, Orte und Eigenschaften in der Vergangenheit.',
    formula: 'I / he / she / it + was   |   you / we / they + were',
    formulaNoteDE:
      'Denk an „you“: Auch wenn du nur EINEN Freund ansprichst, heißt es im Englischen IMMER „you were“ (niemals „you was“!).',
    signalsDiffDE:
      '„could“ (konnte) verhält sich ähnlich stark wie was/were: Es braucht ebenfalls kein „did“.',
    mistakesDE: [
      {
        wrong: 'You was super fast in the parkour race!',
        right: 'You were super fast in the parkour race!',
        note: 'Bei „you“ steht im Standard-Englisch immer „were“.'
      },
      {
        wrong: 'My friends was in the Nether.',
        right: 'My friends were in the Nether.',
        note: '„My friends“ ist Plural (= they) → „were“!'
      }
    ],
    examples: [
      { en: 'I was exhausted after building that giant bridge.', de: 'Ich war erschöpft, nachdem ich diese riesige Brücke gebaut hatte.' },
      { en: 'Our classmates were amazed by the Redstone elevator.', de: 'Unsere Klassenkameraden waren begeistert vom Redstone-Aufzug.' }
    ]
  },
  {
    id: 'was-were-neg-q',
    category: 'was_were',
    title: "wasn't / weren't & Fragen",
    subtitle: "wasn't · weren't · Were you...?",
    badge: 'Kein „did“!',
    whenToUseDE:
      'Um „was“ und „were“ zu verneinen oder Fragen damit zu stellen, brauchst du KEIN „did“! Sie sind stark genug, das selbst zu regeln.',
    formula: "Subjekt + wasn't / weren't   |   Was / Were + Subjekt + ...?",
    formulaNoteDE:
      'Für Fragen wandert „Was“ oder „Were“ einfach ganz nach vorne vor das Subjekt: „You were online.“ → „Were you online?“',
    signalsDiffDE:
      'Dasselbe gilt für „could“: Verneinung „couldn’t“ (nicht „didn’t could“) und Frage „Could you…?“ (nicht „Did you could…?“).',
    mistakesDE: [
      {
        wrong: 'Did you were at school yesterday?',
        right: 'Were you at school yesterday?',
        note: 'Niemals „did“ mit „was/were“ mischen!'
      },
      {
        wrong: "The dungeon didn't be easy.",
        right: "The dungeon wasn't easy.",
        note: 'Verneinung von „be“ ist immer „wasn’t“ oder „weren’t“.'
      }
    ],
    examples: [
      { en: 'Were you scared when the cave noise played?', de: 'Hattest du Angst, als das Höhlengeräusch lief?' },
      { en: "The server wasn't online during maintenance.", de: 'Der Server war während der Wartung nicht online.' }
    ]
  },
  {
    id: 'there-was-were',
    category: 'was_were',
    title: 'There was / There were',
    subtitle: 'Es gab (Einzahl & Mehrzahl)',
    badge: 'Beschreiben',
    whenToUseDE:
      'Perfekt, um deine Minecraft-Welt oder ein Erlebnis zu beschreiben: „Es gab eine Höhle…“ oder „Es waren drei Zombies da…“.',
    formula: 'There was + Einzahl (a/an/one)   |   There were + Mehrzahl (two, many, some...)',
    formulaNoteDE:
      'Verneinung: „There wasn’t any lava.“ / „There weren’t any Creepers.“ Frage: „Was there a chest?“ / „Were there any villagers?“',
    signalsDiffDE:
      'Im Deutschen sagt man immer „Es gab…“ (egal ob ein Creeper oder zehn). Im Englischen musst du genau auf Einzahl (was) vs. Mehrzahl (were) achten!',
    mistakesDE: [
      {
        wrong: 'There was five zombies outside my door.',
        right: 'There were five zombies outside my door.',
        note: 'Fünf Zombies = Plural → „There were“!'
      },
      {
        wrong: 'It gave a big village near spawn.',
        right: 'There was a big village near spawn.',
        note: '„Es gab“ heißt NIEMALS „it gave“, sondern immer „There was / There were“!'
      }
    ],
    examples: [
      { en: 'There was a blacksmith with diamond boots in the village.', de: 'Es gab einen Schmied mit Diamantstiefeln im Dorf.' },
      { en: 'There were twenty torches lighting up the tunnel.', de: 'Es gab zwanzig Fackeln, die den Tunnel beleuchteten.' }
    ]
  },
  {
    id: 'signal-words',
    category: 'traps',
    title: 'Signalwörter (yesterday, ago, last...)',
    subtitle: 'Die Zeitportal-Marker des Past Simple',
    badge: 'Zeit-Kompass',
    whenToUseDE:
      'Signalwörter verraten dir in Tests sofort, dass du das Past Simple benutzen musst. Sie zeigen an, dass ein Zeitpunkt komplett in der Vergangenheit liegt.',
    formula: 'yesterday · last night/week/year · [Zeit] + ago · in 2023 · when I was...',
    formulaNoteDE:
      'Wortstellung im Englischen: Zeitangaben stehen am SATZENDE (oder ganz am Satzanfang) – niemals zwischen Verb und Objekt!',
    signalsDiffDE:
      '„vor zwei Tagen“ = „two days ago“ (ago steht HINTER der Zahl). „letzte Woche“ = „last week“ (OHNE „the“!).',
    mistakesDE: [
      {
        wrong: 'I found ago three days a lush cave.',
        right: 'I found a lush cave three days ago.',
        note: '„ago“ steht hinter der Zeitspanne und die Zeitangabe am Satzende.'
      },
      {
        wrong: 'Yesterday played we Minecraft.',
        right: 'Yesterday, we played Minecraft. / We played Minecraft yesterday.',
        note: 'Im Englischen bleibt immer Subjekt vor Verb (we played)!'
      }
    ],
    examples: [
      { en: 'We defeated the Ender Dragon two weeks ago.', de: 'Wir haben den Enderdrachen vor zwei Wochen besiegt.' },
      { en: 'Last night, I built an automatic bamboo farm.', de: 'Gestern Abend habe ich eine automatische Bambusfarm gebaut.' }
    ]
  },
  {
    id: 'perfect-trap',
    category: 'traps',
    title: 'Die Perfekt-Falle für Deutsche',
    subtitle: 'Past Simple vs. Present Perfect',
    badge: 'Creeper-Falle #1',
    whenToUseDE:
      'Im Deutschen erzählen wir fast alles im Perfekt: „Ich HABE gestern gespielt.“ Wenn du das wörtlich ins Englische übersetzt („I have played yesterday“), explodiert der Satz wie ein Creeper!',
    formula: 'Fester Zeitpunkt in der Vergangenheit (yesterday, last, ago, When...?) → IMMER Past Simple!',
    formulaNoteDE:
      'Das Present Perfect („I have played“) nutzt man im Englischen nur ohne festen Vergangenheitszeitpunkt (z. B. Erfahrungen im Leben: „Have you ever played Minecraft?“).',
    signalsDiffDE:
      'Faustregel für die Schule: Siehst du yesterday, last…, …ago, in 2022 oder When…? → Finger weg von have/has! Nimm Past Simple!',
    mistakesDE: [
      {
        wrong: 'I have built a Redstone door yesterday.',
        right: 'I built a Redstone door yesterday.',
        note: '„yesterday“ + Present Perfect ist im Englischen immer falsch!'
      },
      {
        wrong: 'When have you bought Minecraft?',
        right: 'When did you buy Minecraft?',
        note: '„When…?“ fragt nach einem genauen Zeitpunkt → Past Simple!'
      }
    ],
    examples: [
      { en: 'I visited my grandma last Sunday.', de: 'Ich habe letzten Sonntag meine Oma besucht.' },
      { en: 'We watched a cool Minecraft tutorial ten minutes ago.', de: 'Wir haben vor zehn Minuten ein cooles Minecraft-Tutorial geschaut.' }
    ]
  }
];

// ============================================================================
// 4. IRREGULAR VERBS FORGE: 30 ESSENTIAL A2-B1 IRREGULAR VERBS
// ============================================================================

const IRREGULAR_VERBS = [
  { inf: 'be', past: 'was / were', de: 'sein', example: 'I was in the Nether, and my friends were at base.' },
  { inf: 'build', past: 'built', de: 'bauen', example: 'We built a huge oak castle on the hill.' },
  { inf: 'dig', past: 'dug', de: 'graben', example: 'Leo dug a tunnel down to level -58.' },
  { inf: 'find', past: 'found', de: 'finden', example: 'I found five diamonds in a hidden cave!' },
  { inf: 'go', past: 'went', de: 'gehen', example: 'They went through the End Portal together.' },
  { inf: 'fight', past: 'fought', de: 'kämpfen', example: 'Our team fought the Ender Dragon bravely.' },
  { inf: 'make', past: 'made', de: 'machen / herstellen', example: 'She made a golden apple for the boss fight.' },
  { inf: 'see', past: 'saw', de: 'sehen', example: 'We saw a rare pink sheep near the forest.' },
  { inf: 'get', past: 'got', de: 'bekommen', example: 'Max got a Mending book from the librarian.' },
  { inf: 'have', past: 'had', de: 'haben', example: 'I had only two hearts left!' },
  { inf: 'take', past: 'took', de: 'nehmen', example: 'He took a water bucket before jumping.' },
  { inf: 'give', past: 'gave', de: 'geben', example: 'My friend gave me sixteen iron ingots.' },
  { inf: 'break', past: 'broke', de: 'zerbrechen / abbauen', example: 'My iron pickaxe broke on the last block.' },
  { inf: 'fall', past: 'fell', de: 'fallen', example: 'Oops, I fell into a deep ravine!' },
  { inf: 'buy', past: 'bought', de: 'kaufen', example: 'I bought diamond boots with twelve emeralds.' },
  { inf: 'catch', past: 'caught', de: 'fangen', example: 'We caught three salmon with a fishing rod.' },
  { inf: 'swim', past: 'swam', de: 'schwimmen', example: 'She swam down to the sunken shipwreck.' },
  { inf: 'run', past: 'ran', de: 'rennen', example: 'Everyone ran when the Creeper hissed.' },
  { inf: 'eat', past: 'ate', de: 'essen', example: 'I ate a cooked steak to refill my hunger bar.' },
  { inf: 'drink', past: 'drank', de: 'trinken', example: 'He drank a Fire Resistance potion in the Nether.' },
  { inf: 'write', past: 'wrote', de: 'schreiben', example: 'I wrote our base coordinates in a book.' },
  { inf: 'read', past: 'read (/red/)', de: 'lesen', example: 'We read the Minecraft wiki before the raid.' },
  { inf: 'lose', past: 'lost', de: 'verlieren', example: 'Tom lost his compass in the dark jungle.' },
  { inf: 'win', past: 'won', de: 'gewinnen', example: 'Our squad won three BedWars matches in a row!' },
  { inf: 'come', past: 'came', de: 'kommen', example: 'A wandering trader came to our front gate.' },
  { inf: 'do', past: 'did', de: 'tun / machen', example: 'I did my English homework before gaming.' },
  { inf: 'know', past: 'knew', de: 'wissen / kennen', example: 'She knew the secret Redstone door code.' },
  { inf: 'think', past: 'thought', de: 'denken', example: 'I thought the cave was empty, but it wasn’t!' },
  { inf: 'hear', past: 'heard', de: 'hören', example: 'We heard a spooky cave sound underground.' },
  { inf: 'leave', past: 'left', de: 'verlassen / zurücklassen', example: 'Don’t worry, I left extra torches in your chest.' }
];

// ============================================================================
// 5. PICKAXE RANK SYSTEM
// ============================================================================

const PICKAXE_RANKS = [
  {
    id: 'wood',
    nameDE: 'Holz-Spitzhacke',
    icon: 'pickaxe-wood',
    minRatio: 0,
    colorClass: 'text-amber-500',
    badgeBg: 'bg-amber-950/60 border-amber-600/50',
    messageDE: 'Guter Start im Overworld! Schau kurz in den Crafting-Guide & die Amboss-Tabelle, dann levelst du blitzschnell auf.'
  },
  {
    id: 'stone',
    nameDE: 'Stein-Spitzhacke',
    icon: 'pickaxe-stone',
    minRatio: 0.25,
    colorClass: 'text-slate-300',
    badgeBg: 'bg-slate-800/80 border-slate-500/50',
    messageDE: 'Solide abgebaut! Die ersten Past-Simple-Regeln sitzen schon – jetzt geht’s tiefer in die unregelmäßigen Verben.'
  },
  {
    id: 'iron',
    nameDE: 'Eisen-Spitzhacke',
    icon: 'pickaxe-iron',
    minRatio: 0.5,
    colorClass: 'text-zinc-100',
    badgeBg: 'bg-zinc-800/80 border-zinc-400/50',
    messageDE: 'Starkes Eisen-Upgrade! Über die Hälfte richtig – achte noch kurz auf „didn’t + Grundform“ und „yesterday“.'
  },
  {
    id: 'diamond',
    nameDE: 'Diamant-Spitzhacke',
    icon: 'pickaxe-diamond',
    minRatio: 0.75,
    colorClass: 'text-sky-400',
    badgeBg: 'bg-sky-950/60 border-sky-400/50',
    messageDE: 'Richtig stark! Mit diesem Past-Simple-Skill rockst du die nächste Englisch-Klassenarbeit locker!'
  },
  {
    id: 'netherite',
    nameDE: 'Netherit-Meister',
    icon: 'pickaxe-netherite',
    minRatio: 0.9,
    colorClass: 'text-purple-400',
    badgeBg: 'bg-purple-950/60 border-purple-400/60',
    messageDE: 'Legendär! Absoluter Endboss im Past Simple – unzerstörbar wie Netherit und bereit für jedes Abenteuer!'
  }
];

function getPickaxeRank(correctCount, totalCount) {
  if (!totalCount) return PICKAXE_RANKS[0];
  const ratio = correctCount / totalCount;
  let current = PICKAXE_RANKS[0];
  for (const r of PICKAXE_RANKS) {
    if (ratio >= r.minRatio) {
      current = r;
    }
  }
  return current;
}

// ============================================================================
// 6. MAIN APPLICATION COMPONENT
// ============================================================================

export default function App() {
  // Main Tab: 'quiz' | 'guide'
  const [activeTab, setActiveTab] = useState('quiz');

  // --- QUIZ STATE ---
  const [categoryFilter, setCategoryFilter] = useState('all');
  const [typeFilter, setTypeFilter] = useState('all'); // 'all' | 'fill' | 'four_sentences'
  const [retryMistakesOnly, setRetryMistakesOnly] = useState(false);
  const [retryPool, setRetryPool] = useState([]);

  const [currentIdx, setCurrentIdx] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [score, setScore] = useState(0);
  const [xp, setXp] = useState(0);
  const [streak, setStreak] = useState(0);
  const [bestStreak, setBestStreak] = useState(0);
  const [missedList, setMissedList] = useState([]);
  const [quizFinished, setQuizFinished] = useState(false);

  const [showGermanHint, setShowGermanHint] = useState(false);
  const [autoNext, setAutoNext] = useState(false);

  // --- GUIDE STATE ---
  const [guideSubTab, setGuideSubTab] = useState('recipes'); // 'recipes' | 'forge'
  const [guideCategory, setGuideCategory] = useState('all');
  const [guideSearch, setGuideSearch] = useState('');
  const [activeRecipeModal, setActiveRecipeModal] = useState(null);

  // --- IRREGULAR VERBS FORGE STATE ---
  const [verbSearch, setVerbSearch] = useState('');
  const [hidePastMode, setHidePastMode] = useState(false);
  const [revealedVerbs, setRevealedVerbs] = useState({});

  // Filtered Quiz Deck
  const activeDeck = useMemo(() => {
    if (retryMistakesOnly && retryPool.length > 0) {
      return retryPool;
    }
    return QUIZ_QUESTIONS.filter((q) => {
      const catMatch = categoryFilter === 'all' || q.category === categoryFilter;
      const typeMatch = typeFilter === 'all' || q.type === typeFilter;
      return catMatch && typeMatch;
    });
  }, [categoryFilter, typeFilter, retryMistakesOnly, retryPool]);

  const currentQuestion = activeDeck[currentIdx] || null;
  const isAnswered = selectedOption !== null;

  // Cleanly reset quiz session
  const startNewRun = useCallback(
    (nextCat = categoryFilter, nextType = typeFilter) => {
      setCategoryFilter(nextCat);
      setTypeFilter(nextType);
      setRetryMistakesOnly(false);
      setRetryPool([]);
      setCurrentIdx(0);
      setSelectedOption(null);
      setScore(0);
      setXp(0);
      setStreak(0);
      setBestStreak(0);
      setMissedList([]);
      setQuizFinished(false);
      setShowGermanHint(false);
    },
    [categoryFilter, typeFilter]
  );

  const startRetryMistakes = () => {
    if (missedList.length === 0) return;
    setRetryPool(missedList.map((m) => m.question));
    setRetryMistakesOnly(true);
    setCurrentIdx(0);
    setSelectedOption(null);
    setScore(0);
    setXp(0);
    setStreak(0);
    setBestStreak(0);
    setMissedList([]);
    setQuizFinished(false);
    setShowGermanHint(false);
  };

  const handleNextQuestion = useCallback(() => {
    if (currentIdx < activeDeck.length - 1) {
      setCurrentIdx((prev) => prev + 1);
      setSelectedOption(null);
      setShowGermanHint(false);
    } else {
      setQuizFinished(true);
    }
  }, [currentIdx, activeDeck.length]);

  const handleChooseOption = (optionIndex) => {
    if (isAnswered || !currentQuestion) return;
    setSelectedOption(optionIndex);

    if (optionIndex === currentQuestion.correctIndex) {
      setScore((prev) => prev + 1);
      const nextStreak = streak + 1;
      setStreak(nextStreak);
      setBestStreak((b) => Math.max(b, nextStreak));
      // +20 XP base + 5 XP streak bonus from 3+ streak
      const bonus = nextStreak >= 3 ? 5 : 0;
      setXp((prev) => prev + 20 + bonus);
    } else {
      setStreak(0);
      setMissedList((prev) => [
        ...prev,
        { question: currentQuestion, chosenIndex: optionIndex }
      ]);
    }
  };

  // Optional Auto-Weiter (2,5s) with strict cleanup
  useEffect(() => {
    if (!autoNext || !isAnswered || quizFinished || activeTab !== 'quiz') return;
    const timerId = setTimeout(() => {
      handleNextQuestion();
    }, 2500);
    return () => clearTimeout(timerId);
  }, [autoNext, isAnswered, quizFinished, activeTab, handleNextQuestion]);

  // Keyboard shortcuts: Escape closes modal, Enter advances answered quiz question
  useEffect(() => {
    const onKeyDown = (e) => {
      if (e.key === 'Escape' && activeRecipeModal) {
        setActiveRecipeModal(null);
      } else if (
        e.key === 'Enter' &&
        activeTab === 'quiz' &&
        isAnswered &&
        !quizFinished &&
        !activeRecipeModal
      ) {
        e.preventDefault();
        handleNextQuestion();
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [activeRecipeModal, activeTab, isAnswered, quizFinished, handleNextQuestion]);

  // Filtered Grammar Recipes
  const filteredRecipes = useMemo(() => {
    const q = guideSearch.trim().toLowerCase();
    return GRAMMAR_RECIPES.filter((r) => {
      const catOk = guideCategory === 'all' || r.category === guideCategory;
      const searchOk =
        !q ||
        r.title.toLowerCase().includes(q) ||
        r.subtitle.toLowerCase().includes(q) ||
        r.whenToUseDE.toLowerCase().includes(q) ||
        r.formula.toLowerCase().includes(q);
      return catOk && searchOk;
    });
  }, [guideCategory, guideSearch]);

  // Filtered Irregular Verbs
  const filteredVerbs = useMemo(() => {
    const q = verbSearch.trim().toLowerCase();
    if (!q) return IRREGULAR_VERBS;
    return IRREGULAR_VERBS.filter(
      (v) =>
        v.inf.toLowerCase().includes(q) ||
        v.past.toLowerCase().includes(q) ||
        v.de.toLowerCase().includes(q) ||
        v.example.toLowerCase().includes(q)
    );
  }, [verbSearch]);

  const toggleRevealVerb = (inf) => {
    if (!hidePastMode) return;
    setRevealedVerbs((prev) => ({ ...prev, [inf]: !prev[inf] }));
  };

  const toggleHidePastMode = () => {
    setHidePastMode((prev) => {
      const next = !prev;
      if (next) setRevealedVerbs({});
      return next;
    });
  };

  // Progress & Rank Calculations
  const progressPct = activeDeck.length
    ? Math.round(
        ((quizFinished ? activeDeck.length : currentIdx + (isAnswered ? 1 : 0)) /
          activeDeck.length) *
          100
      )
    : 0;
  const liveRank = getPickaxeRank(score, activeDeck.length);
  const accuracyPct = activeDeck.length
    ? Math.round((score / activeDeck.length) * 100)
    : 0;

  // Render fill-in-the-blank prompt (supports 1 or 2 "_____" blanks cleanly)
  const renderPrompt = (q) => {
    if (q.type !== 'fill') {
      return <span>{q.prompt}</span>;
    }
    const segments = q.prompt.split('_____');
    if (segments.length < 2) return <span>{q.prompt}</span>;

    const chosenRaw = isAnswered ? q.options[selectedOption] : '_____';
    const correctRaw = q.options[q.correctIndex];
    const chosenParts = chosenRaw.includes(' / ') ? chosenRaw.split(' / ') : [chosenRaw];
    const correctParts = correctRaw.includes(' / ') ? correctRaw.split(' / ') : [correctRaw];
    const isCorrect = selectedOption === q.correctIndex;

    return (
      <span>
        {segments.map((seg, idx) => {
          if (idx === segments.length - 1) return <React.Fragment key={idx}>{seg}</React.Fragment>;
          const filledWord = chosenParts[idx] || chosenParts[0];
          const rightWord = correctParts[idx] || correctParts[0];

          let slotClass =
            'inline-block mx-1.5 px-3 py-0.5 rounded border-b-4 font-bold transition-all ';
          if (!isAnswered) {
            slotClass +=
              'bg-sky-500/15 border-sky-400 text-sky-300 min-w-[84px] text-center';
          } else if (isCorrect) {
            slotClass += 'bg-emerald-500/20 border-emerald-400 text-emerald-300';
          } else {
            slotClass += 'bg-red-500/20 border-red-500 text-red-300 line-through';
          }

          return (
            <React.Fragment key={idx}>
              {seg}
              <span className={slotClass}>{filledWord}</span>
              {isAnswered && !isCorrect && (
                <span className="inline-block ml-1 px-2 py-0.5 rounded bg-emerald-500/20 border border-emerald-400/60 text-emerald-300 font-bold text-base">
                  {rightWord}
                </span>
              )}
            </React.Fragment>
          );
        })}
      </span>
    );
  };

  return (
    <div className="min-h-screen bg-[#111318] text-slate-100 font-sans selection:bg-emerald-500/30 selection:text-emerald-200 overflow-x-hidden">
      {/* Voxel Bevel & Pixel Typography Styles */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Silkscreen:wght@400;700&display=swap');
        .font-voxel {
          font-family: 'Silkscreen', ui-monospace, SFMono-Regular, Menlo, monospace;
        }
        .mc-block {
          background-color: #1b1f27;
          border-top: 2px solid #3f4756;
          border-left: 2px solid #3f4756;
          border-right: 2px solid #0b0d12;
          border-bottom: 3px solid #0b0d12;
          box-shadow: 0 10px 24px rgba(0, 0, 0, 0.45);
        }
        .mc-inset {
          background-color: #111318;
          border-top: 2px solid #090b10;
          border-left: 2px solid #090b10;
          border-right: 2px solid #2b313e;
          border-bottom: 2px solid #2b313e;
        }
        .mc-bevel-btn {
          box-shadow:
            inset 2px 2px 0px rgba(255, 255, 255, 0.16),
            inset -2px -3px 0px rgba(0, 0, 0, 0.35);
        }
        .xp-bar-glow {
          box-shadow: 0 0 12px rgba(34, 197, 94, 0.65);
        }
        @keyframes voxelPop {
          from { opacity: 0; transform: translateY(8px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-voxel-pop {
          animation: voxelPop 0.25s ease-out forwards;
        }
      `}</style>

      {/* ====================================================================
          HERO HEADER WITH OVERWORLD & TIME PORTAL BANNER
      ==================================================================== */}
      <header className="relative border-b-4 border-[#0b0d12] bg-[#090b10]">
        <OverworldTimePortalSVG />

        <div className="max-w-5xl mx-auto px-4 sm:px-6 -mt-12 sm:-mt-14 pb-6 relative z-10">
          <div className="mc-block rounded-xl p-5 sm:p-6 flex flex-col md:flex-row md:items-center md:justify-between gap-5">
            <div className="flex items-start gap-4">
              <PixelIconSVG
                type="clock"
                className="w-12 h-12 sm:w-14 sm:h-14 shrink-0 rounded border-2 border-yellow-400/50"
              />
              <div>
                <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-emerald-500/15 border border-emerald-500/40 text-emerald-300 text-xs font-bold uppercase tracking-wider mb-1.5">
                  <Gamepad2 className="w-3.5 h-3.5" />
                  <span>Englisch A2–B1 · Past Simple Edition</span>
                </div>
                <h1 className="text-2xl sm:text-3xl font-voxel tracking-tight text-white leading-snug">
                  Block<span className="text-emerald-400">Craft</span>:{' '}
                  <span className="text-sky-400">Past Simple</span>
                </h1>
                <p className="text-sm text-slate-300 mt-1">
                  Meistere die englische Vergangenheit – 50 Minecraft-Fragen, 12 Rezepte &amp; 30-Verben-Amboss
                </p>
              </div>
            </div>

            {/* 2 Main Navigation Tabs */}
            <nav
              className="flex mc-inset p-1.5 rounded-lg w-full md:w-auto shrink-0"
              aria-label="Hauptnavigation"
            >
              <button
                type="button"
                onClick={() => setActiveTab('quiz')}
                className={`flex-1 md:flex-none flex items-center justify-center gap-2 px-4 py-2.5 rounded text-sm font-bold transition-all cursor-pointer ${
                  activeTab === 'quiz'
                    ? 'bg-emerald-600 text-white mc-bevel-btn'
                    : 'text-slate-300 hover:text-white hover:bg-[#1b1f27]'
                }`}
              >
                <Sparkles className="w-4 h-4 text-yellow-300" />
                <span>Quiz (50 Fragen)</span>
              </button>
              <button
                type="button"
                onClick={() => setActiveTab('guide')}
                className={`flex-1 md:flex-none flex items-center justify-center gap-2 px-4 py-2.5 rounded text-sm font-bold transition-all cursor-pointer ${
                  activeTab === 'guide'
                    ? 'bg-sky-500 text-slate-950 mc-bevel-btn'
                    : 'text-slate-300 hover:text-white hover:bg-[#1b1f27]'
                }`}
              >
                <BookOpen className="w-4 h-4" />
                <span>Crafting-Guide (Past Simple)</span>
              </button>
            </nav>
          </div>
        </div>
      </header>

      {/* ====================================================================
          MAIN CONTENT
      ==================================================================== */}
      <main className="max-w-5xl mx-auto px-4 sm:px-6 py-6 sm:py-8">
        {/* ================================================================
            TAB 1: QUIZ (50 FRAGEN)
        ================================================================ */}
        {activeTab === 'quiz' && (
          <div className="space-y-6 animate-voxel-pop">
            {/* Filters & Controls */}
            <div className="mc-block rounded-xl p-4 sm:p-5 space-y-4">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-sky-400">
                  <Filter className="w-4 h-4" />
                  <span>Kategorien &amp; Modus</span>
                </div>

                <div className="flex flex-wrap items-center gap-2">
                  {/* Auto-Weiter Toggle */}
                  <button
                    type="button"
                    onClick={() => setAutoNext((prev) => !prev)}
                    className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded text-xs font-bold border-2 transition-colors cursor-pointer ${
                      autoNext
                        ? 'bg-emerald-500/20 border-emerald-500 text-emerald-300'
                        : 'bg-[#111318] border-slate-700 text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    <Timer className="w-3.5 h-3.5" />
                    <span>Auto-Weiter (2,5s): {autoNext ? 'AN' : 'AUS'}</span>
                  </button>

                  {/* Reset Run */}
                  <button
                    type="button"
                    onClick={() => startNewRun(categoryFilter, typeFilter)}
                    className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded text-xs font-bold bg-[#111318] border-2 border-slate-700 text-slate-300 hover:border-yellow-400 hover:text-yellow-300 transition-colors cursor-pointer"
                  >
                    <RotateCcw className="w-3.5 h-3.5" />
                    <span>Neuer Run</span>
                  </button>
                </div>
              </div>

              {/* Category Filter Pills */}
              <div className="flex flex-wrap gap-2">
                <button
                  type="button"
                  onClick={() => startNewRun('all', typeFilter)}
                  className={`px-3 py-1.5 rounded text-xs sm:text-sm font-bold border-2 transition-all cursor-pointer ${
                    categoryFilter === 'all' && !retryMistakesOnly
                      ? 'bg-emerald-600 border-emerald-400 text-white mc-bevel-btn'
                      : 'bg-[#111318] border-slate-700 text-slate-300 hover:border-emerald-500/60'
                  }`}
                >
                  Alle ({QUIZ_QUESTIONS.length})
                </button>
                {CATEGORIES.map((cat) => {
                  const count = QUIZ_QUESTIONS.filter((q) => q.category === cat.id).length;
                  const active = categoryFilter === cat.id && !retryMistakesOnly;
                  return (
                    <button
                      key={cat.id}
                      type="button"
                      onClick={() => startNewRun(cat.id, typeFilter)}
                      className={`px-3 py-1.5 rounded text-xs sm:text-sm font-bold border-2 transition-all cursor-pointer ${
                        active
                          ? 'bg-sky-500 border-sky-300 text-slate-950 mc-bevel-btn'
                          : 'bg-[#111318] border-slate-700 text-slate-300 hover:border-sky-400/60'
                      }`}
                    >
                      {cat.labelDE} ({count})
                    </button>
                  );
                })}
              </div>

              {/* Question Type Filter */}
              <div className="flex flex-wrap items-center gap-2 pt-3 border-t border-slate-800">
                <span className="text-xs font-bold text-slate-400 mr-1">Fragetyp:</span>
                {[
                  { id: 'all', label: 'Alle (50)' },
                  { id: 'fill', label: 'Lückentext (35)' },
                  { id: 'four_sentences', label: '4-Sätze-Check (15)' }
                ].map((t) => (
                  <button
                    key={t.id}
                    type="button"
                    onClick={() => startNewRun(categoryFilter, t.id)}
                    className={`px-3 py-1 rounded text-xs font-bold border transition-colors cursor-pointer ${
                      typeFilter === t.id && !retryMistakesOnly
                        ? 'bg-yellow-400/20 border-yellow-400 text-yellow-300'
                        : 'bg-[#111318] border-slate-700 text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    {t.label}
                  </button>
                ))}

                {retryMistakesOnly && (
                  <span className="ml-auto px-2.5 py-1 rounded bg-red-500/20 border border-red-500/50 text-red-300 text-xs font-bold">
                    Fehler-Training ({activeDeck.length} Fragen)
                  </span>
                )}
              </div>
            </div>

            {/* Live XP Bar & Pickaxe Rank HUD */}
            <div className="mc-block rounded-xl p-4 sm:p-5">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-3">
                {/* Pickaxe Rank */}
                <div className="flex items-center gap-3">
                  <PixelIconSVG
                    type={liveRank.icon}
                    className="w-10 h-10 rounded border border-slate-600 shrink-0"
                  />
                  <div>
                    <div className="text-[11px] uppercase tracking-wider text-slate-400 font-bold">
                      Spitzhacken-Rang
                    </div>
                    <div className={`text-sm sm:text-base font-bold ${liveRank.colorClass}`}>
                      {liveRank.nameDE}
                    </div>
                  </div>
                </div>

                {/* Live Counters */}
                <div className="flex flex-wrap items-center gap-2.5">
                  <div className="px-3 py-1.5 rounded mc-inset text-xs sm:text-sm font-bold">
                    Frage{' '}
                    <span className="text-sky-400">
                      {activeDeck.length === 0
                        ? 0
                        : quizFinished
                        ? activeDeck.length
                        : currentIdx + 1}
                    </span>{' '}
                    / {activeDeck.length}
                  </div>

                  <div className="px-3 py-1.5 rounded mc-inset text-xs sm:text-sm font-bold flex items-center gap-1.5">
                    <Trophy className="w-4 h-4 text-yellow-400" />
                    <span className="text-emerald-400">{score}</span>
                    <span className="text-slate-400">({xp} XP)</span>
                  </div>

                  <div
                    className={`px-3 py-1.5 rounded border-2 text-xs sm:text-sm font-bold flex items-center gap-1.5 ${
                      streak >= 3
                        ? 'bg-amber-500/15 border-yellow-400/60 text-yellow-300'
                        : 'mc-inset text-slate-300'
                    }`}
                  >
                    <Flame
                      className={`w-4 h-4 ${
                        streak >= 3 ? 'text-yellow-400' : 'text-slate-500'
                      }`}
                    />
                    <span>{streak}er Serie</span>
                    {streak >= 3 && (
                      <span className="text-[10px] px-1.5 py-0.5 rounded bg-yellow-400 text-slate-950 font-extrabold">
                        +5 XP
                      </span>
                    )}
                  </div>
                </div>
              </div>

              {/* Glowing Green Minecraft XP Bar */}
              <div className="relative h-4 bg-[#090b10] rounded border-2 border-slate-700 overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-emerald-600 via-green-500 to-lime-400 xp-bar-glow transition-all duration-500"
                  style={{ width: `${progressPct}%` }}
                />
                <div className="absolute inset-0 flex justify-between pointer-events-none opacity-35">
                  {Array.from({ length: 10 }).map((_, i) => (
                    <div key={i} className="w-px h-full bg-black" />
                  ))}
                </div>
              </div>
              <div className="flex justify-between text-[11px] text-slate-400 mt-1.5 font-mono">
                <span>Fortschritt: {progressPct}%</span>
                <span>Trefferquote: {accuracyPct}%</span>
              </div>
            </div>

            {/* EMPTY DECK FALLBACK */}
            {activeDeck.length === 0 ? (
              <div className="mc-block rounded-xl p-10 text-center space-y-4">
                <p className="text-slate-300 text-lg">
                  Für diese Filter-Kombination gibt es keine Fragen.
                </p>
                <button
                  type="button"
                  onClick={() => startNewRun('all', 'all')}
                  className="px-5 py-2.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold mc-bevel-btn cursor-pointer"
                >
                  Alle 50 Fragen laden
                </button>
              </div>
            ) : !quizFinished && currentQuestion ? (
              /* ============================================================
                 ACTIVE QUESTION CARD
              ============================================================ */
              <section
                key={currentQuestion.id}
                className="mc-block rounded-xl p-5 sm:p-8 animate-voxel-pop space-y-6"
              >
                {/* Top Meta Row */}
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <div className="flex items-center gap-3">
                    <PixelIconSVG
                      type={CATEGORY_MAP[currentQuestion.category]?.iconType || 'clock'}
                      className="w-11 h-11 rounded border border-slate-600 shrink-0"
                    />
                    <div>
                      <div className="text-xs font-bold uppercase tracking-wider text-emerald-400">
                        {CATEGORY_MAP[currentQuestion.category]?.fullTitleDE}
                      </div>
                      <div className="text-xs text-slate-400 mt-0.5">
                        {currentQuestion.type === 'fill'
                          ? 'Lückentext: Wähle die richtige Past-Simple-Form'
                          : '4-Sätze-Check: Nur EINER der vier Sätze ist grammatisch richtig'}
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    <span
                      className={`px-3 py-1 rounded text-xs font-bold border ${
                        currentQuestion.type === 'four_sentences'
                          ? 'bg-sky-500/15 border-sky-400/50 text-sky-300'
                          : 'bg-yellow-400/15 border-yellow-400/50 text-yellow-300'
                      }`}
                    >
                      {currentQuestion.type === 'four_sentences'
                        ? '4-Sätze-Check'
                        : 'Lückentext'}
                    </span>

                    <button
                      type="button"
                      onClick={() => setShowGermanHint((prev) => !prev)}
                      className={`inline-flex items-center gap-1.5 px-3 py-1 rounded text-xs font-bold border transition-colors cursor-pointer ${
                        showGermanHint
                          ? 'bg-yellow-400 text-slate-950 border-yellow-300'
                          : 'bg-[#111318] border-slate-600 text-yellow-300 hover:border-yellow-400'
                      }`}
                    >
                      <Lightbulb className="w-3.5 h-3.5" />
                      <span>{showGermanHint ? 'Tipp ausblenden' : 'Deutscher Tipp'}</span>
                    </button>
                  </div>
                </div>

                {/* Question Prompt & Optional German Hint */}
                <div className="space-y-3">
                  <h2 className="text-lg sm:text-2xl font-bold text-white leading-relaxed">
                    {renderPrompt(currentQuestion)}
                  </h2>

                  {showGermanHint && (
                    <div className="p-3.5 rounded-lg bg-yellow-400/10 border-l-4 border-yellow-400 text-sm sm:text-base text-yellow-100 animate-voxel-pop">
                      <span className="font-bold text-yellow-300 mr-1.5">Deutscher Tipp:</span>
                      {currentQuestion.germanHint}
                    </div>
                  )}
                </div>

                {/* Clickable Options */}
                <div
                  className={
                    currentQuestion.type === 'four_sentences'
                      ? 'flex flex-col gap-3'
                      : 'grid grid-cols-1 sm:grid-cols-2 gap-3.5'
                  }
                >
                  {currentQuestion.options.map((opt, idx) => {
                    const isCorrectOpt = idx === currentQuestion.correctIndex;
                    const isSelectedOpt = idx === selectedOption;
                    const badgeLetter = String.fromCharCode(65 + idx);

                    let optStyle =
                      'bg-[#111318] border-slate-700 text-slate-100 hover:border-sky-400 hover:bg-[#1f2531]';

                    if (isAnswered) {
                      if (isCorrectOpt) {
                        optStyle =
                          'bg-emerald-500/20 border-emerald-400 text-emerald-100';
                      } else if (isSelectedOpt) {
                        optStyle = 'bg-red-500/20 border-red-500 text-red-100';
                      } else {
                        optStyle =
                          'bg-[#0e1015] border-slate-800 text-slate-500 opacity-60';
                      }
                    }

                    return (
                      <button
                        key={idx}
                        type="button"
                        disabled={isAnswered}
                        onClick={() => handleChooseOption(idx)}
                        className={`w-full rounded-lg border-2 p-4 transition-all duration-150 flex items-start gap-3 text-left whitespace-normal break-words ${
                          isAnswered
                            ? 'cursor-default'
                            : 'cursor-pointer mc-bevel-btn active:translate-y-0.5'
                        } ${optStyle}`}
                      >
                        <span
                          className={`shrink-0 w-7 h-7 rounded flex items-center justify-center text-xs font-voxel font-bold mt-0.5 ${
                            isAnswered && isCorrectOpt
                              ? 'bg-emerald-400 text-slate-950'
                              : isAnswered && isSelectedOpt
                              ? 'bg-red-500 text-white'
                              : 'bg-[#1b1f27] text-sky-300 border border-slate-600'
                          }`}
                        >
                          {badgeLetter}
                        </span>

                        <span className="flex-1 text-sm sm:text-base font-medium leading-snug">
                          {opt}
                        </span>

                        {isAnswered && isCorrectOpt && (
                          <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                        )}
                        {isAnswered && isSelectedOpt && !isCorrectOpt && (
                          <XCircle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
                        )}
                      </button>
                    );
                  })}
                </div>

                {/* Immediate Color-Coded Feedback + Persistent Next Button */}
                {isAnswered && (
                  <div
                    className={`rounded-xl p-5 border-2 animate-voxel-pop flex flex-col sm:flex-row sm:items-center justify-between gap-4 ${
                      selectedOption === currentQuestion.correctIndex
                        ? 'bg-emerald-950/35 border-emerald-500/60'
                        : 'bg-red-950/35 border-red-500/60'
                    }`}
                  >
                    <div className="space-y-1.5 flex-1">
                      <div className="flex items-center gap-2 font-bold text-base">
                        {selectedOption === currentQuestion.correctIndex ? (
                          <>
                            <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                            <span className="text-emerald-300">
                              Stark! +{streak >= 3 ? 25 : 20} XP gesammelt
                            </span>
                          </>
                        ) : (
                          <>
                            <XCircle className="w-5 h-5 text-red-400" />
                            <span className="text-red-300">
                              Creeper-Falle! Schau dir die Regel an:
                            </span>
                          </>
                        )}
                      </div>
                      <p className="text-sm sm:text-base text-slate-200 leading-relaxed">
                        {currentQuestion.explanation}
                      </p>
                    </div>

                    <button
                      type="button"
                      onClick={handleNextQuestion}
                      className="shrink-0 inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm sm:text-base mc-bevel-btn transition-all cursor-pointer active:translate-y-0.5"
                    >
                      <span>
                        {currentIdx < activeDeck.length - 1
                          ? 'Nächste Frage'
                          : 'Ergebnis anzeigen'}
                      </span>
                      <ArrowRight className="w-4 h-4" />
                    </button>
                  </div>
                )}
              </section>
            ) : (
              /* ============================================================
                 END SCREEN: SCORE, XP, PICKAXE RANK & MISSED REVIEW
              ============================================================ */
              <section className="mc-block rounded-xl p-6 sm:p-10 animate-voxel-pop space-y-8">
                <div className="text-center max-w-2xl mx-auto space-y-3">
                  <div className="flex justify-center">
                    <div
                      className={`p-4 rounded-xl border-2 ${liveRank.badgeBg} inline-flex items-center justify-center`}
                    >
                      <PixelIconSVG type={liveRank.icon} className="w-16 h-16" />
                    </div>
                  </div>
                  <div className="text-xs font-bold uppercase tracking-widest text-emerald-400">
                    Zeitportal gemeistert · Dein Rang
                  </div>
                  <h2 className={`text-3xl sm:text-4xl font-voxel ${liveRank.colorClass}`}>
                    {liveRank.nameDE}
                  </h2>
                  <p className="text-slate-300 text-base leading-relaxed">
                    {liveRank.messageDE}
                  </p>
                </div>

                {/* Final Stats */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-2xl mx-auto">
                  <div className="mc-inset rounded-lg p-4 text-center">
                    <div className="text-xs uppercase text-slate-400 font-bold">
                      Ergebnis
                    </div>
                    <div className="text-3xl font-bold text-white mt-1">
                      {score} / {activeDeck.length}
                    </div>
                  </div>
                  <div className="mc-inset rounded-lg p-4 text-center">
                    <div className="text-xs uppercase text-slate-400 font-bold">
                      Gesammelte XP
                    </div>
                    <div className="text-3xl font-bold text-emerald-400 mt-1">
                      {xp} XP
                    </div>
                  </div>
                  <div className="mc-inset rounded-lg p-4 text-center">
                    <div className="text-xs uppercase text-slate-400 font-bold">
                      Beste Serie
                    </div>
                    <div className="text-3xl font-bold text-yellow-400 mt-1">
                      {bestStreak}
                    </div>
                  </div>
                </div>

                {/* Action Buttons */}
                <div className="flex flex-wrap items-center justify-center gap-3">
                  {missedList.length > 0 && (
                    <button
                      type="button"
                      onClick={startRetryMistakes}
                      className="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold mc-bevel-btn transition-all cursor-pointer"
                    >
                      <RefreshCw className="w-4 h-4" />
                      <span>Nur Fehler wiederholen ({missedList.length})</span>
                    </button>
                  )}

                  <button
                    type="button"
                    onClick={() => startNewRun('all', 'all')}
                    className="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold mc-bevel-btn transition-all cursor-pointer"
                  >
                    <RotateCcw className="w-4 h-4" />
                    <span>Neuer Run</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => setActiveTab('guide')}
                    className="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-[#111318] hover:bg-slate-800 text-sky-300 font-bold border-2 border-slate-600 transition-all cursor-pointer"
                  >
                    <BookOpen className="w-4 h-4" />
                    <span>Zum Crafting-Guide</span>
                  </button>
                </div>

                {/* Review of Missed Questions */}
                {missedList.length > 0 && (
                  <div className="pt-6 border-t-2 border-slate-800 space-y-4">
                    <h3 className="text-lg sm:text-xl font-bold text-white flex items-center gap-2">
                      <AlertTriangle className="w-5 h-5 text-yellow-400" />
                      <span>Fehler-Analyse ({missedList.length} Fragen)</span>
                    </h3>

                    <div className="space-y-3.5">
                      {missedList.map(({ question, chosenIndex }) => (
                        <div
                          key={question.id}
                          className="mc-inset rounded-lg p-4 sm:p-5 space-y-2.5"
                        >
                          <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
                            <span className="font-bold text-sky-400 uppercase">
                              Frage #{question.id} ·{' '}
                              {CATEGORY_MAP[question.category]?.labelDE}
                            </span>
                            <span className="text-slate-400">
                              {question.type === 'four_sentences'
                                ? '4-Sätze-Check'
                                : 'Lückentext'}
                            </span>
                          </div>
                          <p className="text-white font-semibold leading-relaxed">
                            {question.prompt}
                          </p>
                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-sm">
                            <div className="p-3 rounded bg-red-950/50 border border-red-500/40 text-red-200">
                              <span className="block text-xs font-bold uppercase text-red-400 mb-1">
                                Deine Antwort:
                              </span>
                              {question.options[chosenIndex]}
                            </div>
                            <div className="p-3 rounded bg-emerald-950/50 border border-emerald-500/40 text-emerald-200">
                              <span className="block text-xs font-bold uppercase text-emerald-400 mb-1">
                                Richtige Antwort:
                              </span>
                              {question.options[question.correctIndex]}
                            </div>
                          </div>
                          <p className="text-sm text-slate-300 leading-relaxed pt-1">
                            {question.explanation}
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </section>
            )}
          </div>
        )}

        {/* ================================================================
            TAB 2: CRAFTING-GUIDE (12 REZEPTE + 30-VERBEN-AMBOSS)
        ================================================================ */}
        {activeTab === 'guide' && (
          <div className="space-y-6 animate-voxel-pop">
            {/* Sub-Tab Switcher inside Crafting-Guide */}
            <div className="mc-block rounded-xl p-4 sm:p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <PixelIconSVG
                  type={guideSubTab === 'recipes' ? 'enchanted-book' : 'anvil'}
                  className="w-11 h-11 rounded border border-slate-600 shrink-0"
                />
                <div>
                  <h2 className="text-xl sm:text-2xl font-voxel text-white">
                    {guideSubTab === 'recipes'
                      ? 'Grammatik-Rezepte'
                      : 'Amboss-Tabelle: 30 Verben'}
                  </h2>
                  <p className="text-sm text-slate-400">
                    {guideSubTab === 'recipes'
                      ? '12 detaillierte Past-Simple-Regeln mit Creeper-Fallen & Beispielen'
                      : '30 wichtige unregelmäßige Verben mit Lernmodus zum Selbsttesten'}
                  </p>
                </div>
              </div>

              <div className="flex mc-inset p-1 rounded-lg shrink-0">
                <button
                  type="button"
                  onClick={() => setGuideSubTab('recipes')}
                  className={`flex-1 sm:flex-none inline-flex items-center justify-center gap-2 px-4 py-2 rounded text-xs sm:text-sm font-bold transition-all cursor-pointer ${
                    guideSubTab === 'recipes'
                      ? 'bg-emerald-600 text-white mc-bevel-btn'
                      : 'text-slate-300 hover:text-white'
                  }`}
                >
                  <BookOpen className="w-4 h-4" />
                  <span>12 Grammatik-Rezepte</span>
                </button>
                <button
                  type="button"
                  onClick={() => setGuideSubTab('forge')}
                  className={`flex-1 sm:flex-none inline-flex items-center justify-center gap-2 px-4 py-2 rounded text-xs sm:text-sm font-bold transition-all cursor-pointer ${
                    guideSubTab === 'forge'
                      ? 'bg-sky-500 text-slate-950 mc-bevel-btn'
                      : 'text-slate-300 hover:text-white'
                  }`}
                >
                  <Hammer className="w-4 h-4" />
                  <span>Amboss (30 Verben)</span>
                </button>
              </div>
            </div>

            {/* ------------------------------------------------------------
                SUB-VIEW A: 12 GRAMMAR RECIPE CARDS
            ------------------------------------------------------------ */}
            {guideSubTab === 'recipes' && (
              <div className="space-y-5">
                {/* Search & Category Cards */}
                <div className="mc-block rounded-xl p-4 sm:p-5 space-y-4">
                  <div className="relative w-full sm:max-w-md">
                    <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
                    <input
                      type="text"
                      value={guideSearch}
                      onChange={(e) => setGuideSearch(e.target.value)}
                      placeholder="Regel suchen: didn't, yesterday, was/were..."
                      className="w-full pl-10 pr-4 py-2.5 rounded-lg bg-[#111318] border-2 border-slate-700 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-sky-400 transition-colors"
                    />
                  </div>

                  <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5">
                    <button
                      type="button"
                      onClick={() => setGuideCategory('all')}
                      className={`p-3 rounded-lg border-2 text-left transition-all cursor-pointer flex flex-col justify-between ${
                        guideCategory === 'all'
                          ? 'bg-emerald-500/20 border-emerald-400 text-white'
                          : 'bg-[#111318] border-slate-700 text-slate-300 hover:border-slate-500'
                      }`}
                    >
                      <PixelIconSVG type="clock" className="w-8 h-8 mb-2" />
                      <div>
                        <div className="font-bold text-sm">Alle ({GRAMMAR_RECIPES.length})</div>
                        <div className="text-[11px] text-slate-400">Komplettes Buch</div>
                      </div>
                    </button>

                    {CATEGORIES.map((cat) => {
                      const active = guideCategory === cat.id;
                      const count = GRAMMAR_RECIPES.filter((r) => r.category === cat.id).length;
                      return (
                        <button
                          key={cat.id}
                          type="button"
                          onClick={() => setGuideCategory(cat.id)}
                          className={`p-3 rounded-lg border-2 text-left transition-all cursor-pointer flex flex-col justify-between ${
                            active
                              ? 'bg-sky-500/20 border-sky-400 text-white'
                              : 'bg-[#111318] border-slate-700 text-slate-300 hover:border-sky-400/50'
                          }`}
                        >
                          <PixelIconSVG type={cat.iconType} className="w-8 h-8 mb-2" />
                          <div>
                            <div className="font-bold text-sm leading-tight">{cat.labelDE}</div>
                            <div className="text-[11px] text-slate-400 mt-0.5">
                              {count} {count === 1 ? 'Rezept' : 'Rezepte'}
                            </div>
                          </div>
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* Recipe Cards Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {filteredRecipes.map((recipe) => (
                    <button
                      key={recipe.id}
                      type="button"
                      onClick={() => setActiveRecipeModal(recipe)}
                      className="mc-block rounded-xl p-5 text-left hover:border-sky-400 hover:-translate-y-0.5 transition-all duration-150 cursor-pointer group flex flex-col justify-between gap-4"
                    >
                      <div>
                        <div className="flex items-center justify-between gap-2 mb-3">
                          <span className="text-[11px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded bg-[#111318] text-emerald-300 border border-slate-700">
                            {recipe.badge}
                          </span>
                          <PixelIconSVG
                            type={CATEGORY_MAP[recipe.category]?.iconType || 'clock'}
                            className="w-7 h-7 rounded"
                          />
                        </div>

                        <h3 className="text-lg sm:text-xl font-extrabold text-white group-hover:text-sky-300 transition-colors">
                          {recipe.title}
                        </h3>
                        <p className="text-xs sm:text-sm font-semibold text-yellow-300 mt-1 font-mono">
                          {recipe.subtitle}
                        </p>
                        <p className="text-xs sm:text-sm text-slate-300 mt-2.5 line-clamp-2 leading-relaxed">
                          {recipe.whenToUseDE}
                        </p>
                      </div>

                      <div className="pt-3 border-t border-slate-800 flex items-center justify-between text-xs font-bold text-sky-400">
                        <span>Alle 5 Abschnitte öffnen</span>
                        <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                      </div>
                    </button>
                  ))}
                </div>

                {filteredRecipes.length === 0 && (
                  <div className="mc-block rounded-xl p-10 text-center text-slate-400">
                    Kein Rezept für „{guideSearch}“ gefunden. Probier ein anderes Suchwort!
                  </div>
                )}
              </div>
            )}

            {/* ------------------------------------------------------------
                SUB-VIEW B: IRREGULAR VERBS FORGE (30 VERBS + HIDE/REVEAL)
            ------------------------------------------------------------ */}
            {guideSubTab === 'forge' && (
              <div className="mc-block rounded-xl p-4 sm:p-6 space-y-5 animate-voxel-pop">
                {/* Forge Controls */}
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-3">
                  <div className="relative flex-1 max-w-md">
                    <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
                    <input
                      type="text"
                      value={verbSearch}
                      onChange={(e) => setVerbSearch(e.target.value)}
                      placeholder="Verb suchen: build, dug, kämpfen..."
                      className="w-full pl-10 pr-4 py-2.5 rounded-lg bg-[#111318] border-2 border-slate-700 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-sky-400 transition-colors"
                    />
                  </div>

                  <div className="flex flex-wrap items-center gap-2">
                    <button
                      type="button"
                      onClick={toggleHidePastMode}
                      className={`inline-flex items-center gap-2 px-4 py-2.5 rounded-lg text-xs sm:text-sm font-bold border-2 transition-all cursor-pointer mc-bevel-btn ${
                        hidePastMode
                          ? 'bg-yellow-400 text-slate-950 border-yellow-300'
                          : 'bg-[#111318] text-yellow-300 border-yellow-400/50 hover:border-yellow-400'
                      }`}
                    >
                      {hidePastMode ? (
                        <EyeOff className="w-4 h-4" />
                      ) : (
                        <Eye className="w-4 h-4" />
                      )}
                      <span>
                        Verben abdecken (Lernmodus): {hidePastMode ? 'AN' : 'AUS'}
                      </span>
                    </button>

                    {hidePastMode && (
                      <button
                        type="button"
                        onClick={() => setRevealedVerbs({})}
                        className="px-3 py-2.5 rounded-lg text-xs font-bold bg-[#111318] border-2 border-slate-700 text-slate-300 hover:border-sky-400 cursor-pointer"
                      >
                        Alle wieder zudecken
                      </button>
                    )}
                  </div>
                </div>

                {hidePastMode && (
                  <div className="p-3 rounded-lg bg-sky-500/10 border border-sky-400/40 text-xs sm:text-sm text-sky-200 flex items-center gap-2">
                    <Clock className="w-4 h-4 text-sky-400 shrink-0" />
                    <span>
                      <strong>Lernmodus aktiv!</strong> Sag dir die 2. Form laut vor und klicke
                      auf eine Zeile, um die Lösung aufzudecken.
                    </span>
                  </div>
                )}

                {/* Responsive Table */}
                <div className="overflow-x-auto mc-inset rounded-lg">
                  <table className="w-full text-left border-collapse">
                    <thead>
                      <tr className="border-b-2 border-slate-800 bg-[#181c24] text-xs uppercase tracking-wider text-slate-400">
                        <th className="py-3 px-4 font-bold">Infinitiv (1. Form)</th>
                        <th className="py-3 px-4 font-bold text-emerald-400">
                          Past Simple (2. Form)
                        </th>
                        <th className="py-3 px-4 font-bold">Deutsch</th>
                        <th className="py-3 px-4 font-bold hidden md:table-cell">
                          Minecraft-Beispiel
                        </th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-800/80 text-sm">
                      {filteredVerbs.map((v) => {
                        const isHidden = hidePastMode && !revealedVerbs[v.inf];
                        return (
                          <tr
                            key={v.inf}
                            onClick={() => toggleRevealVerb(v.inf)}
                            className={`transition-colors ${
                              hidePastMode
                                ? 'cursor-pointer hover:bg-sky-500/10'
                                : 'hover:bg-slate-800/40'
                            }`}
                          >
                            <td className="py-3 px-4 font-bold text-white font-mono">
                              {v.inf}
                            </td>
                            <td className="py-3 px-4">
                              {isHidden ? (
                                <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-slate-800 border border-slate-600 text-xs font-bold text-yellow-300">
                                  <Eye className="w-3.5 h-3.5" />
                                  <span>Klicken zum Aufdecken</span>
                                </span>
                              ) : (
                                <span className="inline-block px-2.5 py-0.5 rounded bg-emerald-500/15 border border-emerald-500/40 text-emerald-300 font-bold font-mono">
                                  {v.past}
                                </span>
                              )}
                            </td>
                            <td className="py-3 px-4 text-slate-300">{v.de}</td>
                            <td className="py-3 px-4 text-slate-400 italic hidden md:table-cell">
                              {isHidden ? '••••••••••••••••••••' : v.example}
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>

                {filteredVerbs.length === 0 && (
                  <p className="text-center text-slate-400 py-6">
                    Kein Verb für „{verbSearch}“ gefunden.
                  </p>
                )}
              </div>
            )}
          </div>
        )}
      </main>

      {/* ====================================================================
          DETAILED RECIPE MODAL (5 STRUCTURED GERMAN SECTIONS)
      ==================================================================== */}
      {activeRecipeModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/80 backdrop-blur-sm animate-voxel-pop"
          onClick={() => setActiveRecipeModal(null)}
          role="dialog"
          aria-modal="true"
          aria-labelledby="recipe-modal-title"
        >
          <div
            className="w-full max-w-3xl max-h-[90vh] overflow-y-auto mc-block rounded-xl border-2 border-sky-400/70 p-5 sm:p-8 relative"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Close Button */}
            <button
              type="button"
              onClick={() => setActiveRecipeModal(null)}
              aria-label="Fenster schließen"
              className="absolute top-4 right-4 w-10 h-10 rounded-lg bg-[#111318] border-2 border-slate-700 text-slate-300 hover:text-white hover:border-red-500 flex items-center justify-center transition-colors cursor-pointer"
            >
              <X className="w-5 h-5" />
            </button>

            {/* Modal Header */}
            <div className="flex items-start gap-4 pr-12 pb-5 border-b-2 border-slate-800">
              <PixelIconSVG
                type={CATEGORY_MAP[activeRecipeModal.category]?.iconType || 'clock'}
                className="w-14 h-14 rounded border border-slate-600 shrink-0 hidden sm:block"
              />
              <div>
                <div className="flex flex-wrap items-center gap-2 mb-1.5">
                  <span className="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-500/20 border border-emerald-500/40 text-emerald-300">
                    {CATEGORY_MAP[activeRecipeModal.category]?.labelDE}
                  </span>
                  <span className="px-2.5 py-0.5 rounded text-xs font-bold bg-sky-500/15 border border-sky-400/40 text-sky-300">
                    {activeRecipeModal.badge}
                  </span>
                </div>
                <h2
                  id="recipe-modal-title"
                  className="text-2xl sm:text-3xl font-extrabold text-white"
                >
                  {activeRecipeModal.title}
                </h2>
                <p className="text-sm sm:text-base font-bold text-yellow-300 font-mono mt-1">
                  {activeRecipeModal.subtitle}
                </p>
              </div>
            </div>

            {/* 5 Structured German Sections */}
            <div className="space-y-4 mt-6">
              {/* 1. Wann benutzt man es? */}
              <div className="mc-inset rounded-lg p-4 sm:p-5">
                <h3 className="text-xs sm:text-sm font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-2 mb-2">
                  <GraduationCap className="w-4 h-4" />
                  <span>1. Wann benutzt man es? (Bedeutung &amp; Einsatz)</span>
                </h3>
                <p className="text-sm sm:text-base text-slate-200 leading-relaxed">
                  {activeRecipeModal.whenToUseDE}
                </p>
              </div>

              {/* 2. Crafting-Formel */}
              <div className="mc-inset rounded-lg p-4 sm:p-5">
                <h3 className="text-xs sm:text-sm font-bold uppercase tracking-wider text-sky-400 flex items-center gap-2 mb-2.5">
                  <Sparkles className="w-4 h-4" />
                  <span>2. Crafting-Formel (Satzbau &amp; Bildung)</span>
                </h3>
                <div className="font-mono text-xs sm:text-sm bg-[#090b10] border border-sky-400/40 text-sky-200 px-3.5 py-2.5 rounded mb-3 break-words">
                  {activeRecipeModal.formula}
                </div>
                <p className="text-sm sm:text-base text-slate-200 leading-relaxed">
                  {activeRecipeModal.formulaNoteDE}
                </p>
              </div>

              {/* 3. Signalwörter & Unterschiede */}
              <div className="mc-inset rounded-lg p-4 sm:p-5">
                <h3 className="text-xs sm:text-sm font-bold uppercase tracking-wider text-yellow-400 flex items-center gap-2 mb-2">
                  <Scale className="w-4 h-4" />
                  <span>3. Signalwörter &amp; Unterschiede</span>
                </h3>
                <p className="text-sm sm:text-base text-slate-200 leading-relaxed">
                  {activeRecipeModal.signalsDiffDE}
                </p>
              </div>

              {/* 4. Creeper-Falle: Typische Fehler für Deutsche */}
              <div className="rounded-lg bg-red-950/25 border-2 border-red-500/40 p-4 sm:p-5">
                <h3 className="text-xs sm:text-sm font-bold uppercase tracking-wider text-red-400 flex items-center gap-2 mb-3">
                  <AlertTriangle className="w-4 h-4" />
                  <span>4. Creeper-Falle: Typische Fehler für Deutsche (❌ vs. ✅)</span>
                </h3>
                <div className="space-y-3">
                  {activeRecipeModal.mistakesDE.map((m, idx) => (
                    <div
                      key={idx}
                      className="rounded bg-[#090b10]/90 border border-slate-800 p-3.5 space-y-1.5 text-sm"
                    >
                      <div className="text-red-300">
                        <span className="font-bold mr-1.5">❌</span>
                        <span className="line-through opacity-90">{m.wrong}</span>
                      </div>
                      <div className="text-emerald-300">
                        <span className="font-bold mr-1.5">✅</span>
                        <span className="font-semibold">{m.right}</span>
                      </div>
                      <p className="text-xs sm:text-sm text-slate-400 pt-1">{m.note}</p>
                    </div>
                  ))}
                </div>
              </div>

              {/* 5. Minecraft-Beispiele */}
              <div className="mc-inset rounded-lg p-4 sm:p-5">
                <h3 className="text-xs sm:text-sm font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-2 mb-3">
                  <Gamepad2 className="w-4 h-4" />
                  <span>5. Minecraft-Beispiele (Englisch + Deutsch)</span>
                </h3>
                <div className="space-y-3">
                  {activeRecipeModal.examples.map((ex, idx) => (
                    <div
                      key={idx}
                      className="rounded bg-[#181c24] border-l-4 border-emerald-400 p-3.5"
                    >
                      <p className="text-sm sm:text-base font-bold text-white leading-snug">
                        {ex.en}
                      </p>
                      <p className="text-xs sm:text-sm text-slate-400 italic mt-1">
                        {ex.de}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}