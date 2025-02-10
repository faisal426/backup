import os
import time
import requests

def get_current_ip():
    try:
        session = requests.Session()
        session.proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
        ip = session.get("https://api64.ipify.org?format=json").json()["ip"]
        return ip
    except Exception as e:
        return f"Gagal mendapatkan IP: {e}"

while True:
    print(f"IP saat ini: {get_current_ip()}")
    os.system("killall -HUP tor")  # Restart TOR buat dapetin IP baru
    time.sleep(1)  # Tunggu 1 detik sebelum ngecek IP baru
    print(f"IP baru: {get_current_ip()}")
