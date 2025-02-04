#!/bin/bash

# Menambahkan perubahan
git add .

# Commit dengan pesan "backup"
git commit -m "backup"

# Push ke branch master
git push origin master

# Tampilkan pesan backup selesai dengan warna hijau cerah pada latar belakang hitam
echo -e "\e[1;92m\e[40mBackup selesai!\e[0m"
