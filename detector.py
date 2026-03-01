# detector.py

import re
import time
import subprocess
import requests
from datetime import datetime, timedelta
from collections import defaultdict

import config
from logger import setup_logger

logging = setup_logger()

failed_attempts = defaultdict(list)
blocked_ips = {}

# ==============================
# TELEGRAM ALERT
# ==============================

def send_telegram_alert(message):
    if not config.TELEGRAM_ENABLED:
        return

    try:
        url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": message
        }
        requests.post(url, data=payload, timeout=5)
    except Exception as e:
        logging.error(f"Telegram alert failed: {e}")

# ==============================
# BLOCK IP
# ==============================

def block_ip(ip):
    try:
        subprocess.run(
            ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )
        blocked_ips[ip] = datetime.now()

        logging.warning(f"IP BLOCKED: {ip}")
        send_telegram_alert(f"🚨 SSH Brute Force Detected\nIP Blocked: {ip}")

    except Exception as e:
        logging.error(f"Failed to block IP {ip}: {e}")

# ==============================
# UNBLOCK EXPIRED IPs
# ==============================

def unblock_expired_ips():
    now = datetime.now()

    for ip, block_time in list(blocked_ips.items()):
        if now - block_time > timedelta(minutes=config.BLOCK_DURATION_MINUTES):
            try:
                subprocess.run(
                    ["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
                    check=True
                )
                del blocked_ips[ip]
                logging.info(f"IP UNBLOCKED: {ip}")
                send_telegram_alert(f"✅ IP Unblocked: {ip}")
            except Exception as e:
                logging.error(f"Failed to unblock IP {ip}: {e}")

# ==============================
# HANDLE FAILED LOGIN
# ==============================

def handle_failed_attempt(ip):
    now = datetime.now()

    # Clean old attempts
    failed_attempts[ip] = [
        t for t in failed_attempts[ip]
        if now - t < timedelta(minutes=config.ATTEMPT_WINDOW_MINUTES)
    ]

    failed_attempts[ip].append(now)

    logging.warning(f"Failed login from {ip} | Attempts: {len(failed_attempts[ip])}")

    if len(failed_attempts[ip]) >= config.FAILED_THRESHOLD and ip not in blocked_ips:
        block_ip(ip)

# ==============================
# ANALYZE LOG LINE
# ==============================

def analyze_line(line):
    failed_match = re.search(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)", line)
    success_match = re.search(r"Accepted password.*from (\d+\.\d+\.\d+\.\d+)", line)

    if failed_match:
        ip = failed_match.group(1)
        handle_failed_attempt(ip)

    elif success_match:
        ip = success_match.group(1)
        logging.info(f"Successful login from {ip}")
        send_telegram_alert(f"🔐 Successful SSH Login from {ip}")

# ==============================
# FOLLOW LOG FILE
# ==============================

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(config.CHECK_INTERVAL)
            continue
        yield line