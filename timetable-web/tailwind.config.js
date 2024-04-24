/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    screens: {
      'md': '820px',
      // => @media (min-width: 640px) { ... }

      'lg': '920px',
      // => @media (min-width: 900px) { ... }

      'xl': '1150px',
      // => @media (min-width: 1150px) { ... }

      'desktop': '1280px',
      // => @media (min-width: 1280px) { ... }
    },
  },
  plugins: [],
}

