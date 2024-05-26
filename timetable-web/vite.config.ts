import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": {
        target: "http://backend:8000", //"http://backend:8000" when runnning with docker
        changeOrigin: true,            //"http://127.0.0.1:8000" when runnning locally
        rewrite: (path) => path.replace(/^\/api/, "")
      }
    }
  }
})
