-- ======================================
-- Smart Lab Management System (SLMS)
-- Database Schema
-- ======================================

CREATE DATABASE IF NOT EXISTS slms_db;
USE slms_db;

-- جدول المستخدمين
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('student', 'admin') NOT NULL
);

-- جدول الأجهزة
CREATE TABLE devices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status ENUM('available', 'reserved', 'maintenance') DEFAULT 'available'
);

-- جدول الحجوزات
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    device_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (device_id) REFERENCES devices(id)
);

-- بيانات تجريبية
INSERT INTO users (username, password, role) VALUES
('admin1', 'admin123', 'admin'),
('student1', 'pass123', 'student'),
('student2', 'pass123', 'student');

INSERT INTO devices (name, status) VALUES
('PC-01', 'available'),
('PC-02', 'available'),
('PC-03', 'maintenance'),
('PC-04', 'available'),
('PC-05', 'reserved');
