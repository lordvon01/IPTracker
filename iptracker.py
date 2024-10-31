import requests
import schedule
import time
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
IP_API = "https://api.ipify.org?format=json"
CHECK_INTERVAL = 10  # in minutes

# Email configuration from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Store the last known IP address
last_ip = None

def get_external_ip():
    """Fetch the current external IP address."""
    try:
        response = requests.get(IP_API)
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None

def send_email_notification(new_ip):
    """Send an email notification when the IP changes."""
    subject = "IP Address Change Notification"
    body = f"Your IP address has changed to: {new_ip}"
    
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_ip_change():
    """Check for IP change and send notification if it changes."""
    global last_ip
    current_ip = get_external_ip()
    if current_ip and current_ip != last_ip:
        print(f"IP changed from {last_ip} to {current_ip}")
        send_email_notification(current_ip)
        last_ip = current_ip
    else:
        print("No IP change detected.")

# Schedule the IP check
schedule.every(CHECK_INTERVAL).minutes.do(check_ip_change)

# Run the scheduled checks
while True:
    schedule.run_pending()
    time.sleep(1)
