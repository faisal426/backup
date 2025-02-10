import os
import time
import requests

def get_current_ip():
    try:
        session = requests.Session()
        session.proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
        ip = session.get("https://api64.ipify.org?format=json").json()["ip"]
        return ip
    except:
        return "Tidak dapat mengambil IP"

# Memulai layanan TOR di Termux
os.system("tor &")
time.sleep(10)  # Tunggu TOR berjalan

while True:
    print(f"IP saat ini: {get_current_ip()}")
    os.system("killall -HUP tor")  # Restart TOR untuk mendapatkan IP baru
    time.sleep(10)  # Tunggu perubahan IP
    print(f"IP baru: {get_current_ip()}")
    time.sleep(60)  # Tunggu 1 menit sebelum update berikutnya
