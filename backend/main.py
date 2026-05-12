from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "username": "student1", "password": "1234", "role": "Student"},
    {"id": 2, "username": "admin", "password": "admin123", "role": "Admin"},
]

devices = [
    {"id": 1, "name": "Computer 1", "status": "Available"},
    {"id": 2, "name": "Computer 2", "status": "Reserved"},
    {"id": 3, "name": "Microscope 1", "status": "Available"},
]

@app.route("/")
def home():
    return jsonify({"message": "Lab Management System is running!"})

@app.route("/devices")
def get_devices():
    return jsonify(devices)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:
            return jsonify({"message": "Login successful!", "role": user["role"]})

    return jsonify({"message": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run(debug=True)
