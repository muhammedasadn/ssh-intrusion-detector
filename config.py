# config.py

# ==============================
# SYSTEM CONFIGURATION
# ==============================

LOG_FILE = "/var/log/auth.log"

FAILED_THRESHOLD = 5
ATTEMPT_WINDOW_MINUTES = 10
BLOCK_DURATION_MINUTES = 30

CHECK_INTERVAL = 0.2

# ==============================
# TELEGRAM CONFIG
# ==============================

TELEGRAM_ENABLED = True
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"