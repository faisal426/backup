#!/bin/bash

# Menambahkan perubahan
git add .

# Commit dengan pesan "backup"
git commit -m "backup"

# Push ke branch master
git push origin master

# Tampilkan pesan backup selesai dengan warna hijau
echo "Backup selesai!"
