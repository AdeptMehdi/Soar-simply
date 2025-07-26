import time
import re
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Any
import json
import os
from datetime import datetime
from colorama import init, Fore, Style

# === Configuration ===
LOG_FILE = 'sample.log'  # Path to the log file to monitor
KEYWORDS = [
    {'keyword': 'failed login', 'severity': 'high', 'category': 'Authentication'},
    {'keyword': 'unauthorized', 'severity': 'high', 'category': 'Authorization'},
    {'keyword': 'error', 'severity': 'medium', 'category': 'General'},
    {'keyword': 'attack', 'severity': 'high', 'category': 'Malware'},
    {'keyword': 'malware', 'severity': 'high', 'category': 'Malware'},
]  # Suspicious keywords with metadata
EMAIL_ALERTS = False  # Set to True to enable email alerts
EMAIL_TO = 'admin@example.com'
EMAIL_FROM = 'soar@example.com'
SMTP_SERVER = 'localhost'
SMTP_PORT = 25
EVENTS_DB = 'events.json'  # File to store detected events
POLL_INTERVAL = 1.0  # Seconds between log file checks

# === Color Setup ===
init(autoreset=True)
SEVERITY_COLOR = {
    'high': Fore.RED + Style.BRIGHT,
    'medium': Fore.YELLOW + Style.BRIGHT,
    'low': Fore.CYAN + Style.BRIGHT
}
INFO_COLOR = Fore.CYAN + Style.BRIGHT
WARN_COLOR = Fore.YELLOW + Style.BRIGHT
ERROR_COLOR = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

# === Data Structures ===
def load_events() -> List[Dict[str, Any]]:
    if not os.path.exists(EVENTS_DB):
        return []
    with open(EVENTS_DB, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except Exception:
            return []

def save_event(event: Dict[str, Any]):
    events = load_events()
    events.append(event)
    with open(EVENTS_DB, 'w', encoding='utf-8') as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

# === Functions ===
def send_email_alert(subject: str, body: str):
    if not EMAIL_ALERTS:
        return
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string())
        print(INFO_COLOR + f"[EMAIL] Alert sent to {EMAIL_TO}" + RESET)
    except Exception as e:
        print(ERROR_COLOR + f"[EMAIL ERROR] {e}" + RESET)

def analyze_line(line: str) -> List[Dict[str, Any]]:
    """Return list of matched keyword dicts in the line."""
    matches = [kw for kw in KEYWORDS if re.search(re.escape(kw['keyword']), line, re.IGNORECASE)]
    return matches

def create_event(line: str, matches: List[Dict[str, Any]]) -> Dict[str, Any]:
    now = datetime.now().isoformat()
    return {
        'timestamp': now,
        'line': line.strip(),
        'matches': matches,
        'severity': max((m['severity'] for m in matches), key=lambda s: ['low','medium','high'].index(s)),
        'categories': list(set(m['category'] for m in matches)),
    }

def monitor_log():
    print(INFO_COLOR + f"[SOAR] Monitoring log file: {LOG_FILE}" + RESET)
    last_inode = None
    last_size = 0
    try:
        while True:
            try:
                stat = os.stat(LOG_FILE)
                inode = getattr(stat, 'st_ino', None)
                size = stat.st_size
                if inode != last_inode:
                    f = open(LOG_FILE, 'r')
                    f.seek(0, 2)
                    last_inode = inode
                    last_size = f.tell()
                else:
                    f = open(LOG_FILE, 'r')
                    f.seek(last_size)
                while True:
                    line = f.readline()
                    if not line:
                        break
                    matches = analyze_line(line)
                    if matches:
                        event = create_event(line, matches)
                        sev = event['severity']
                        color = SEVERITY_COLOR.get(sev, Fore.WHITE)
                        alert_msg = (f"{color}[ALERT]{RESET} "
                                     f"{event['timestamp']} | "
                                     f"Severity: {color}{sev.upper()}{RESET} | "
                                     f"Categories: {Fore.MAGENTA}{event['categories']}{RESET} | "
                                     f"Line: {Fore.WHITE}{event['line']}{RESET}")
                        print(alert_msg)
                        save_event(event)
                        send_email_alert("SOAR Alert", alert_msg)
                last_size = f.tell()
                f.close()
            except FileNotFoundError:
                print(ERROR_COLOR + f"[ERROR] Log file {LOG_FILE} not found." + RESET)
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print(INFO_COLOR + "[SOAR] Stopped." + RESET)

def show_events():
    events = load_events()
    if not events:
        print(INFO_COLOR + "[SOAR] No events recorded." + RESET)
        return
    print(INFO_COLOR + f"[SOAR] Showing {len(events)} recorded events:" + RESET)
    for i, event in enumerate(events, 1):
        sev = event['severity']
        color = SEVERITY_COLOR.get(sev, Fore.WHITE)
        print(f"{color}{i}. {event['timestamp']} | Severity: {sev.upper()} | Categories: {event['categories']} | Line: {event['line']}{RESET}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'show':
        show_events()
    else:
        monitor_log() 