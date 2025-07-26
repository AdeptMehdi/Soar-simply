# SOAR Simple

**A Lightweight Security Orchestration, Automation & Response Tool for Blue Teams**

---

## Overview
SOAR Simple is a minimal, fast, and easy-to-use tool for monitoring log files, detecting suspicious security events, and automating responses. Designed for blue teams, it helps you stay alert and react quickly to incidents with a colorful CLI and simple configuration.

---

## Features
- Real-time log file monitoring
- Event analysis and categorization (Severity/Category)
- Colorful CLI alerts for quick visibility
- Event storage in JSON for later review
- Optional email alerting (configurable)
- View and search recorded events

---

## Installation
1. Clone the repository:
   ```bash
   git clone <REPO_URL>
   cd <REPO_DIR>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Place a log file (e.g., `sample.log`) next to the script, or change the file name in the config section of `soar_simple.py`.
2. Start monitoring:
   ```bash
   python soar_simple.py
   ```
3. View recorded events:
   ```bash
   python soar_simple.py show
   ```

---

## Configuration
- Edit keywords, severity, and categories at the top of `soar_simple.py`.
- To enable email alerts, set `EMAIL_ALERTS = True` and configure SMTP settings.

---

## Contributing
Pull requests and suggestions are welcome!

---

## License
MIT

---

# سوار سیمپل (SOAR Simple)

**ابزار سبک مدیریت و پاسخ خودکار به رخدادهای امنیتی برای تیم آبی**

---

## معرفی
SOAR Simple یک ابزار سریع و ساده برای مانیتورینگ فایل لاگ، شناسایی رخدادهای مشکوک امنیتی و پاسخ خودکار است. این ابزار برای تیم آبی طراحی شده تا با رابط رنگی و پیکربندی آسان، همیشه آماده واکنش سریع به رخدادها باشید.

---

## امکانات
- مانیتورینگ بلادرنگ فایل لاگ
- تحلیل و دسته‌بندی رخدادها (شدت/دسته)
- هشدار رنگی در ترمینال برای دیده شدن سریع
- ذخیره رخدادها در فایل JSON برای بررسی بعدی
- امکان ارسال هشدار ایمیلی (قابل تنظیم)
- مشاهده و جستجوی رخدادهای ثبت‌شده

---

## نصب
1. کلون پروژه:
   ```
   git clone <REPO_URL>
   cd <REPO_DIR>
   ```
2. نصب پیش‌نیازها:
   ```
   pip install -r requirements.txt
   ```

---

## استفاده
1. یک فایل لاگ (مثلاً `sample.log`) کنار اسکریپت قرار دهید یا نام آن را در ابتدای `soar_simple.py` تغییر دهید.
2. اجرای مانیتورینگ:
   ```
   python soar_simple.py
   ```
3. مشاهده رخدادهای ثبت‌شده:
   ```
   python soar_simple.py show
   ```

---

## تنظیمات
- کلمات کلیدی، شدت و دسته‌بندی در ابتدای فایل `soar_simple.py` قابل ویرایش است.
- برای فعال‌سازی هشدار ایمیلی، مقدار `EMAIL_ALERTS` را `True` قرار دهید و تنظیمات SMTP را وارد کنید.

---

## مشارکت
پیشنهادها و Pull Requestها خوش‌آمدند!

---

## لایسنس
MIT 