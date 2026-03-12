# Real-Time SSH Detector

## Overview

Real-Time SSH Detector is a cybersecurity tool designed to monitor SSH login activities on Linux systems and detect suspicious access attempts in real time.

The system analyzes authentication logs and identifies patterns such as multiple failed login attempts, brute-force attacks, or unauthorized access attempts. When suspicious activity is detected, it logs the event and alerts the system administrator.

This project helps improve server security by providing early detection of potential intrusion attempts.

---

## Features

- Real-time monitoring of SSH login activity
- Detection of multiple failed login attempts
- Identification of possible brute-force attacks
- Security alert generation
- Log analysis for authentication events
- Lightweight and easy to deploy

---

## Technologies Used

- Python
- Linux System Logs
- SSH Authentication Logs
- Bash / Shell Commands

---

## How It Works

1. The system continuously monitors SSH authentication logs.
2. It scans login attempts and tracks failed authentication events.
3. If repeated failed attempts occur within a short time frame, it flags the activity as suspicious.
4. The system logs the event and optionally generates alerts.

This helps system administrators respond quickly to potential intrusion attempts.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/muhammedasadn/Real_time_ssh_detector.git
