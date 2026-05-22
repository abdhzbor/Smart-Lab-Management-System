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

@app.route("/book", methods=["POST"])
def book_device():
    data = request.get_json()
    user_id = data.get("user_id")
    device_id = data.get("device_id")
    time_start = data.get("time_start")
    time_end = data.get("time_end")
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT status FROM devices WHERE id=%s", (device_id,))
    device = cursor.fetchone()
    if not device:
        return jsonify({"message": "Device not found"}), 404
    if device["status"] != "Available":
        return jsonify({"message": "Device is not available"}), 400
    cursor.execute("INSERT INTO reservations (user_id, device_id, time_start, time_end) VALUES (%s, %s, %s, %s)", (user_id, device_id, time_start, time_end))
    cursor.execute("UPDATE devices SET status='Reserved' WHERE id=%s", (device_id,))
    db.commit()
    db.close()
    return jsonify({"message": "Device booked successfully!"})

@app.route("/reservations")
def get_reservations():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    db.close()
    return jsonify(reservations)
@app.route("/devices/add", methods=["POST"])
def add_device():
    data = request.get_json()
    name = data.get("name")
    category = data.get("category")
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO devices (name, status, category) VALUES (%s, 'Available', %s)", (name, category))
    db.commit()
    db.close()
    return jsonify({"message": "Device added successfully!"})

@app.route("/devices/delete/<int:device_id>", methods=["DELETE"])
def delete_device(device_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM devices WHERE id=%s", (device_id,))
    db.commit()
    db.close()
    return jsonify({"message": "Device deleted successfully!"})
if __name__ == "__main__":
    app.run(debug=True)
