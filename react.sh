#!/bin/bash

# Pindah ke direktori proyek
cd ~/vite-project || { echo "Direktori tidak ditemukan"; exit 1; }

# Jalankan proyek
echo "Menjalankan proyek ReactJs..."
npm run dev
