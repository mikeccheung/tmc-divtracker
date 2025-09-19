/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#1a56db',
          light: '#3b82f6',
          dark: '#1e3a8a'
        }
      }
    }
  },
  plugins: []
};
