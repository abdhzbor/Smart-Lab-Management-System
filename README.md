# 🧪 Smart Lab Management System (SLMS)
### نظام إدارة المختبر الذكي

> نظام ويب متكامل يعتمد على نموذج **Client-Server** يتيح للطلاب حجز أجهزة المختبر، ويمكّن المشرفين من إدارة الأجهزة ومراقبة الاستخدام بشكل مركزي وفعّال.

---

## 📌 جدول المحتويات

- [وصف المشروع](#-وصف-المشروع)
- [التقنيات المستخدمة](#️-التقنيات-المستخدمة)
- [هيكل المشروع](#-هيكل-المشروع)
- [قاعدة البيانات](#️-قاعدة-البيانات)
- [الـ Backend](#-الـ-backend)
- [الـ Frontend](#-الـ-frontend)
- [طريقة تشغيل المشروع](#-طريقة-تشغيل-المشروع)
- [الـ APIs المتاحة](#-الـ-apis-المتاحة)
- [فريق العمل](#-فريق-العمل)

---

## 📋 وصف المشروع

يهدف النظام إلى حل مشكلة الفوضى في إدارة المختبرات الجامعية من خلال:

- ✅ تمكين الطلاب من **حجز الأجهزة** إلكترونياً
- ✅ تمكين المشرفين من **إدارة الأجهزة** وعرض جميع الحجوزات
- ✅ منع **تعارض الحجوزات** تلقائياً
- ✅ توفير **واجهة مستخدم** سهلة وواضحة

---

## 🛠️ التقنيات المستخدمة

| القسم | التقنية | الإصدار |
|-------|---------|---------|
| Backend | Python / Flask | 3.x |
| Database | MySQL | 8.0 |
| Cloud Database | Railway.app | - |
| Authentication | Flask-JWT-Extended | - |
| Password Hashing | Flask-Bcrypt | - |
| Frontend | HTML / CSS / JavaScript | - |
| Version Control | Git / GitHub | - |

---

## 📁 هيكل المشروع

```
Smart-Lab-Management-System/
│
├── backend/
│   ├── main.py              # السيرفر الرئيسي Flask
│   └── venv/                # البيئة الافتراضية
│
├── database/
│   ├── schema.sql           # هيكل قاعدة البيانات الكامل
│   └── README.md            # معلومات الاتصال بقاعدة البيانات
│
├── templates/
│   ├── login.html           # صفحة تسجيل الدخول
│   ├── dashboard.html       # لوحة تحكم الطالب
│   ├── devices.html         # عرض الأجهزة
│   ├── book.html            # نموذج الحجز
│   ├── confirm.html         # تأكيد الحجز
│   ├── admin.html           # لوحة تحكم المشرف
│   └── 404.html             # صفحة الخطأ
│
├── static/
│   └── style.css            # ملف التنسيقات
│
└── README.md
```

---

## 🗄️ قاعدة البيانات

### الجداول الرئيسية

#### جدول المستخدمين — `users`
| الحقل | النوع | الوصف |
|-------|-------|-------|
| id | INT / PK | معرّف فريد |
| username | VARCHAR(50) | اسم الدخول |
| password | VARCHAR(255) | كلمة المرور المشفّرة |
| role | ENUM | Student / Admin / Supervisor / Technician |

#### جدول الأجهزة — `devices`
| الحقل | النوع | الوصف |
|-------|-------|-------|
| id | INT / PK | معرّف فريد |
| name | VARCHAR(100) | اسم الجهاز (مثال: PC-01) |
| status | ENUM | Available / Reserved / Maintenance |
| category | VARCHAR(50) | تصنيف الجهاز |

#### جدول الحجوزات — `reservations`
| الحقل | النوع | الوصف |
|-------|-------|-------|
| id | INT / PK | معرّف فريد |
| user_id | INT / FK | مَن قام بالحجز |
| device_id | INT / FK | الجهاز المحجوز |
| time_start | DATETIME | وقت بداية الحجز |
| time_end | DATETIME | وقت نهاية الحجز |

### إنشاء قاعدة البيانات
```bash
mysql -u root -p < database/schema.sql
```

---

## ⚙️ الـ Backend

### المكتبات المستخدمة
```
Flask               — إطار العمل الرئيسي
PyMySQL             — للتواصل مع MySQL
Flask-JWT-Extended  — نظام المصادقة بالـ Token
Flask-Bcrypt        — تشفير كلمات المرور
Flask-CORS          — السماح بطلبات الـ Frontend
```

### نظام الصلاحيات
| الصلاحية | Student | Admin |
|----------|---------|-------|
| تسجيل الدخول | ✅ | ✅ |
| عرض الأجهزة | ✅ | ✅ |
| حجز جهاز | ✅ | ✅ |
| إضافة جهاز | ❌ | ✅ |
| حذف جهاز | ❌ | ✅ |
| عرض كل الحجوزات | ❌ | ✅ |

---

## 🎨 الـ Frontend

- 7 صفحات HTML متكاملة
- تصميم موحّد باستخدام `style.css`
- ربط ديناميكي مع الـ Backend عبر JavaScript
- تمييز لوني لحالات الأجهزة (متاح / محجوز / صيانة)

---

## 🚀 طريقة تشغيل المشروع

### المتطلبات الأساسية
- Python 3.x
- MySQL 8.0
- Git

---

### الخطوة 1 — استنساخ المستودع
```bash
git clone https://github.com/abdhzbor/Smart-Lab-Management-System.git
cd Smart-Lab-Management-System
```

---

### الخطوة 2 — إعداد قاعدة البيانات
```bash
# الدخول إلى MySQL
sudo mysql -u root -p

# تشغيل ملف الـ Schema
SOURCE database/schema.sql;

# التحقق
SHOW DATABASES;
USE lab_management;
SHOW TABLES;
```

---

### الخطوة 3 — إعداد الـ Backend
```bash
# الانتقال لمجلد الـ Backend
cd backend

# إنشاء البيئة الافتراضية
python3 -m venv venv

# تفعيل البيئة
source venv/bin/activate        # على Linux/Mac
venv\Scripts\activate           # على Windows

# تثبيت المكتبات
pip install Flask PyMySQL Flask-JWT-Extended Flask-Bcrypt Flask-CORS
```

---

### الخطوة 4 — تشغيل السيرفر
```bash
python3 main.py
```

السيرفر يعمل على:
```
http://127.0.0.1:5000
```

---

### الخطوة 5 — فتح المشروع
افتح المتصفح وانتقل إلى:
```
http://127.0.0.1:5000
```

#### بيانات الدخول التجريبية
| المستخدم | كلمة المرور | الدور |
|----------|------------|-------|
| admin1 | admin123 | Admin |
| student1 | pass123 | Student |
| student2 | pass123 | Student |

---

## 🔌 الـ APIs المتاحة

| المسار | الطريقة | الوظيفة | الصلاحية |
|--------|---------|---------|---------|
| `/` | GET | التحقق من تشغيل السيرفر | الكل |
| `/login` | POST | تسجيل الدخول والحصول على Token | الكل |
| `/devices` | GET | عرض جميع الأجهزة | مسجّل دخول |
| `/book` | POST | حجز جهاز | مسجّل دخول |
| `/reservations` | GET | عرض الحجوزات | مسجّل دخول |
| `/devices/add` | POST | إضافة جهاز | Admin فقط |
| `/devices/delete/<id>` | DELETE | حذف جهاز | Admin فقط |

---

## 👥 فريق العمل

| القسم | المهام |
|-------|--------|
| 🗄️ Database | تصميم الجداول، إدارة MySQL، النشر على Railway |
| ⚙️ Backend | Flask APIs، JWT، نظام الصلاحيات، منطق الحجز |
| 🎨 Frontend | صفحات HTML/CSS، الربط مع الـ Backend |

---

## 🔗 روابط مفيدة

- [Flask Documentation](https://flask.palletsprojects.com)
- [MySQL Documentation](https://dev.mysql.com/doc)
- [Railway Dashboard](https://railway.app)
- [JWT Documentation](https://flask-jwt-extended.readthedocs.io)

---

> **ملاحظة:** هذا المشروع تم تطويره كمتطلب لمادة برمجة التطبيقات الشبكية — 2026
