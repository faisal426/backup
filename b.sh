#!/bin/bash

# Cek apakah ada direktori .git di dalam direktori saat ini
if [ ! -d ".git" ]; then
    echo "Error: Direktori ini bukan repositori Git!"
    exit 1
fi

# Menambahkan perubahan
git add .

# Commit dengan pesan "backup"
git commit -m "backup"

# Push ke branch master
git push -u origin master

# Tampilkan pesan backup selesai dengan warna hijau
echo -e "\e[32mBackup selesai!\e[0m"
