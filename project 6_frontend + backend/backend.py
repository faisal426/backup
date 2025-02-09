from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Koneksi ke database
def connect():
    return sqlite3.connect("database.db")

# Buat tabel jika belum ada
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

# API: Ambil semua data
@app.route("/users", methods=["GET"])
def get_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    
    return jsonify(users)

# API: Tambah user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (nama, usia) VALUES (?, ?)", (data["nama"], data["usia"]))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User berhasil ditambahkan!"})

# API: Hapus user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User berhasil dihapus!"})

# API: Update user
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET nama = ?, usia = ? WHERE id = ?", (data["nama"], data["usia"], id))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User berhasil diperbarui!"})

if __name__ == "__main__":
    init_db()  # Buat database jika belum ada
    app.run(host="0.0.0.0", port=5000, debug=True)
