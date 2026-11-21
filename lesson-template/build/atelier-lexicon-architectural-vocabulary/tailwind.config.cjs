// The page's own Tailwind config, moved out of source.html, where it ran through
// Tailwind's CDN compiler in every visitor's browser. Values unchanged.
module.exports = {
  content: ['./page.build.html'],
  theme: {
    extend: {
      colors: {
        alabaster: '#F7F5F0',
        parchment: '#EFECE4',
        paper: '#FCFBF8',
        charcoal: '#1E1E1C',
        graphite: '#56544F',
        stone: '#8C877E',
        hairline: '#E2DDD5',
        terracotta: '#B85D3B',
        'terracotta-dark': '#96482B',
        'terracotta-soft': '#F5E7E1',
        sage: '#4A7C59',
        'sage-soft': '#E6F0E9',
      },
      fontFamily: {
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        sans: ['"Inter"', 'system-ui', '-apple-system', 'sans-serif'],
      },
      boxShadow: {
        editorial: '0 1px 2px rgba(30, 30, 28, 0.04), 0 8px 24px -12px rgba(30, 30, 28, 0.08)',
        card: '0 2px 6px rgba(30, 30, 28, 0.04), 0 12px 30px -15px rgba(30, 30, 28, 0.1)',
      },
      keyframes: {
        fadeUp: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        softPop: {
          '0%': { transform: 'scale(0.985)' },
          '50%': { transform: 'scale(1.012)' },
          '100%': { transform: 'scale(1)' },
        },
        subtleShake: {
          '0%, 100%': { transform: 'translateX(0)' },
          '25%': { transform: 'translateX(-4px)' },
          '75%': { transform: 'translateX(4px)' },
        },
      },
      animation: {
        'fade-up': 'fadeUp 0.35s cubic-bezier(0.22, 1, 0.36, 1) forwards',
        'soft-pop': 'softPop 0.28s ease-out',
        'subtle-shake': 'subtleShake 0.28s ease-in-out',
      },
    },
  },
  plugins: [],
};
