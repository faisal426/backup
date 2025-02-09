import sqlite3

# Koneksi ke database
def connect():
    return sqlite3.connect("database.db")

# Buat Tabel (Jika Belum Ada)
def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        usia INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Tambah Data
def insert_user(nama, usia):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (nama, usia) VALUES (?, ?)", (nama, usia))
    conn.commit()
    conn.close()
    print(f"User {nama} berhasil ditambahkan!")

# Baca Data
def get_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    for user in users:
        print(user)

# Update Data
def update_user(id_user, nama_baru, usia_baru):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET nama = ?, usia = ? WHERE id = ?", (nama_baru, usia_baru, id_user))
    conn.commit()
    conn.close()
    print(f"User ID {id_user} berhasil diperbarui!")

# Hapus Data
def delete_user(id_user):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id_user,))
    conn.commit()
    conn.close()
    print(f"User ID {id_user} berhasil dihapus!")

# Menu CLI di Termux
def main():
    init_db()
    while True:
        print("\n===== MENU CRUD SQLITE =====")
        print("1. Tambah User")
        print("2. Lihat Semua User")
        print("3. Update User")
        print("4. Hapus User")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            nama = input("Masukkan Nama: ")
            usia = input("Masukkan Usia: ")
            insert_user(nama, int(usia))
        elif pilihan == "2":
            get_users()
        elif pilihan == "3":
            id_user = input("Masukkan ID yang ingin diupdate: ")
            nama_baru = input("Nama Baru: ")
            usia_baru = input("Usia Baru: ")
            update_user(int(id_user), nama_baru, int(usia_baru))
        elif pilihan == "4":
            id_user = input("Masukkan ID yang ingin dihapus: ")
            delete_user(int(id_user))
        elif pilihan == "5":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
