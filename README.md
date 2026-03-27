# 🔐 Real-Time SSH Intrusion Detection System

> A lightweight, real-time intrusion detection tool for monitoring SSH authentication activity and identifying brute-force or suspicious login attempts on Linux systems.

---

## 📌 Overview

Real-Time SSH IDS is a cybersecurity-focused system that continuously monitors SSH authentication logs to detect potential intrusion attempts such as brute-force attacks and unauthorized access patterns.

The system is designed with a focus on **real-time detection**, **low resource usage**, and **practical deployment in Linux environments**.

It helps system administrators gain visibility into login activity and respond quickly to security threats.

---

## ⚡ Key Highlights

- 🔍 Real-time SSH log monitoring  
- 🚨 Detection of brute-force and suspicious login patterns  
- 📊 Event logging for security auditing  
- ⚙️ Lightweight and efficient (minimal system overhead)  
- 🐧 Designed for Linux-based systems  
- 🧠 Pattern-based anomaly detection  

---

## 🧠 Problem Statement

SSH is one of the most common attack surfaces in Linux systems.  
Brute-force attacks and unauthorized access attempts often go unnoticed until damage occurs.

### This project solves:
- Lack of real-time monitoring  
- Delayed response to attacks  
- Poor visibility into authentication activity  

---

## 🏗️ System Architecture
    ┌──────────────────────────┐
    │  SSH Authentication Log  │
    │  (/var/log/auth.log)     │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │   Log Monitoring Engine  │
    │  (File Watcher / Tail)   │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │   Detection Engine       │
    │  (Pattern Recognition)   │
    └────────────┬─────────────┘
                 │
    ┌────────────┴─────────────┐
    ▼                          ▼
┌───────────────┐ ┌────────────────┐
│ Alert System  │ │ Event Logging  │
│ (Console/Log) │ │ (Audit Trail)  │
└───────────────┘ └────────────────┘

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Environment:** Linux  
- **Logs:** `/var/log/auth.log`  
- **Tools:** Bash, System Utilities  

---

## 🔍 Detection Logic

The system identifies suspicious activity using:

- Multiple failed login attempts within a time window  
- Repeated attempts from the same IP  
- Unusual login patterns  

### Example Logic:
IF failed_attempts > threshold within time_window:
FLAG as suspicious

---

## 🚀 Features

- Continuous log monitoring (real-time)  
- Failed login tracking  
- Brute-force detection heuristics  
- Alert generation system  
- Security event logging  
- Easy deployment on Linux servers  

---

## 🛠️ Installation & Setup

Clone the repository:

`bash
git clone https://github.com/muhammedasadn/Real_time_ssh_detector.git
cd Real_time_ssh_detector`
Run the application:

`python main.py`

⚠️ Requires Linux system with access to authentication logs

📌 Use Cases
🛡 Detect SSH brute-force attacks
🖥 Monitor server login activity
🔐 Improve Linux server security posture
🎓 Learn real-world cybersecurity monitoring
📈 Future Enhancements
📲 Telegram / Email alert integration
🌐 Web-based dashboard (real-time visualization)
🚫 Automatic IP blocking (Fail2Ban integration)
🧩 SIEM integration (Splunk, ELK stack)
📊 Advanced anomaly detection using Machine Learning
🧪 Engineering Improvements
Implement async log streaming for better performance
Add sliding window algorithms for detection accuracy
Introduce modular plugin architecture
Optimize memory and CPU usage

# screenshots
<img width="1003" height="176" alt="Screenshot from 2026-03-27 15-17-58" src="https://github.com/user-attachments/assets/93ec6f31-ac10-421e-9ced-d431dc155ce1" />

<img width="1019" height="132" alt="Screenshot from 2026-03-27 15-28-16" src="https://github.com/user-attachments/assets/9c9b67de-5c4d-4980-9ee0-25ce5c0d0ebd" />



👨‍💻 Author

Muhammed Asad N
Backend Developer | Cybersecurity Enthusiast

📄 License

This project is licensed under the MIT License
