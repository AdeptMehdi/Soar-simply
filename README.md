<p align="center">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/microsoftdefender.svg" alt="SOAR Simple Logo" width="120"/>
</p>

<h1 align="center">🛡️ SOAR Simple</h1>
<p align="center">
  <b>A Lightweight, Colorful, and Cross-Platform Security Orchestration, Automation & Response Tool for Blue Teams</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-windows%20%7C%20linux-blue"/>
  <img src="https://img.shields.io/badge/python-3.7%2B-brightgreen"/>
  <img src="https://img.shields.io/badge/license-MIT-yellow"/>
  <img src="https://img.shields.io/badge/status-active-success"/>
</p>

---

## 🚀 Overview
SOAR Simple is a minimal, fast, and easy-to-use tool for monitoring log files, detecting suspicious security events, and automating responses. Designed for blue teams, it helps you stay alert and react quickly to incidents with a colorful CLI, web dashboard, and simple configuration.

---

## ✨ Features

| Feature                        | Description                                                      |
|--------------------------------|------------------------------------------------------------------|
| 🔎 Real-time Monitoring        | Watch multiple log files for suspicious events                    |
| 🧠 Event Analysis              | Categorize and score events by severity and type                  |
| 🎨 Colorful CLI                | Alerts and logs with severity-based colors                        |
| 🗃️ Event Storage               | Store events in JSON/SQLite for later review                      |
| 📧 Email & Webhook Alerts      | Optional email and Slack notifications                            |
| 🖥️ Web Dashboard (Flask)       | Modern dashboard for stats and event review                       |
| ⚡ Automated Response          | Run scripts (Linux/Windows), block IPs, custom actions            |
| 🪟 Cross-Platform              | Works on Windows (batch) and Linux/Mac (shell)                    |

---

## 🛠️ Installation
```bash
# Clone the repository
$ git clone https://github.com/AdeptMehdi/Soar-simply.git
$ cd Soar-simply

# Install dependencies
$ pip install -r requirements.txt
```

---

## 🚦 Usage
```bash
# Start monitoring and web dashboard
python soar_advanced.py

# Just the dashboard
python soar_advanced.py web

# Show events in CLI
python soar_advanced.py show

# Show statistics
python soar_advanced.py stats
```

---

## ⚙️ Configuration
- **Rules & Actions:** Edit `config/rules.json` (regex, categories, actions, etc.)
- **Email Alerts:** Set `enabled` to `true` in the `email` action and configure SMTP.
- **Automated Response:**
  - Linux/Mac: Use `scripts/response.sh`
  - Windows: Use `scripts/response.bat` (set path in `rules.json`)

---

## 🪟 Windows Support
- All features work on Windows.
- Use `scripts/response.bat` for automated responses (logging, notifications, block IPs with admin rights).
- Set the batch script path in `rules.json` for Windows actions.

---

## 🤝 Contributing
Pull requests and suggestions are welcome!

---

## 📄 License
MIT

---

---

<p align="center">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/microsoftdefender.svg" alt="SOAR Simple Logo" width="100"/>
</p>

<h1 align="center">🛡️ سوار سیمپل</h1>
<p align="center">
  <b>ابزار سبک، رنگی و چندسکویی مدیریت و پاسخ خودکار به رخدادهای امنیتی برای تیم آبی</b>
</p>

---

## ✨ امکانات

| قابلیت                        | توضیح                                                        |
|-------------------------------|--------------------------------------------------------------|
| 🔎 مانیتورینگ بلادرنگ         | پایش چندین فایل لاگ برای رخدادهای مشکوک                      |
| 🧠 تحلیل رخداد                | دسته‌بندی و امتیازدهی رخدادها بر اساس شدت و نوع              |
| 🎨 هشدار رنگی                 | هشدارها و لاگ‌ها با رنگ‌بندی بر اساس شدت                     |
| 🗃️ ذخیره رخداد                | ذخیره رخدادها در JSON یا دیتابیس برای بررسی بعدی              |
| 📧 هشدار ایمیل و وب‌هوک        | ارسال هشدار به ایمیل یا Slack (در صورت تنظیم)                |
| 🖥️ داشبورد وب (Flask)         | داشبورد مدرن برای آمار و مرور رخدادها                        |
| ⚡ پاسخ خودکار                 | اجرای اسکریپت (لینوکس/ویندوز)، بلاک IP، اکشن سفارشی          |
| 🪟 پشتیبانی ویندوز            | همه امکانات روی ویندوز (اسکریپت batch) و لینوکس/مک (shell)   |

---

## 🛠️ نصب
```bash
# کلون پروژه
git clone https://github.com/AdeptMehdi/Soar-simply.git
cd Soar-simply

# نصب پیش‌نیازها
pip install -r requirements.txt
```

---

## 🚦 استفاده
```bash
# اجرای مانیتورینگ و داشبورد وب
python soar_advanced.py

# فقط داشبورد
python soar_advanced.py web

# نمایش رخدادها در CLI
python soar_advanced.py show

# نمایش آمار
python soar_advanced.py stats
```

---

## ⚙️ تنظیمات
- **قوانین و اکشن‌ها:** در `config/rules.json` ویرایش کنید (regex، دسته‌بندی، اکشن و ...)
- **هشدار ایمیلی:** مقدار `enabled` را در بخش `email` روی `true` بگذارید و SMTP را تنظیم کنید.
- **پاسخ خودکار:**
  - لینوکس/مک: `scripts/response.sh`
  - ویندوز: `scripts/response.bat` (وارد کردن مسیر در rules.json)

---

## 🪟 پشتیبانی ویندوز
- همه امکانات اصلی روی ویندوز هم کار می‌کند.
- برای پاسخ خودکار، از اسکریپت batch (`scripts/response.bat`) استفاده کنید و مسیر آن را در rules.json قرار دهید.
- نمونه اسکریپت batch برای لاگ‌کردن، ارسال نوتیفیکیشن و بلاک IP (با دسترسی ادمین) آماده است.

---

## 🤝 مشارکت
پیشنهادها و Pull Requestها خوش‌آمدند!

---

## 📄 لایسنس
MIT
