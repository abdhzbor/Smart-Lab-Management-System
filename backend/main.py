from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='lab_management',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    return jsonify({"message": "Lab Management System is running!"})

@app.route("/devices")
def get_devices():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    db.close()
    return jsonify(devices)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    db.close()
    if user:
        return jsonify({"message": "Login successful!", "role": user["role"]})
    return jsonify({"message": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run(debug=True)
