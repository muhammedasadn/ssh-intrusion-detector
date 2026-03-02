# main.py

from detector import follow, analyze_line, unblock_expired_ips
import config
from logger import setup_logger

logging = setup_logger()

def main():
    print("=== SSH Detector Started ===")
    logging.info("SSH Detector Started")

    try:
        with open(config.LOG_FILE, "r") as file:
            loglines = follow(file)
            for line in loglines:
                analyze_line(line)
                unblock_expired_ips()

    except Exception as e:
        logging.critical(f"Fatal error: {e}")
        print("Critical error occurred. Check logs.")

if __name__ == "__main__":
    main()