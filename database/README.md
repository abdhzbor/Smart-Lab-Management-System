# Database - Smart Lab Management System

## معلومات الاتصال
| المعلومة | القيمة |
|----------|--------|
| Database | lab_management |
| User     | slms_user |
| Password | slms2026 |
| Host     | localhost |
| Port     | 3306 |

## تشغيل الـ Database من الصفر
```bash
sudo mysql -u root -p < database/schema.sql
```

## الجداول
| الجدول | الوصف |
|--------|-------|
| users | بيانات المستخدمين |
| devices | الأجهزة المتاحة في المختبر |
| reservations | سجل الحجوزات |

## الأدوار المتاحة (roles)
- Admin
- Student
- Supervisor
- Technician
