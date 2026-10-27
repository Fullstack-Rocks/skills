import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import { viteSingleFile } from 'vite-plugin-singlefile'

// One self-contained index.html, so serve.py and export.py ship a single file and users never need Node.
export default defineConfig({
  plugins: [react(), viteSingleFile()],
  build: { outDir: 'dist', emptyOutDir: true },
})
