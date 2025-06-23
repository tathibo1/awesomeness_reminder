import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from recipient_manager import get_recipients

load_dotenv()

def send_message(body):
    from_email = os.getenv("FROM_EMAIL")
    password = os.getenv("GOOGLE_APP_PASSWORD")
    subject = "Awesomeness Reminder"
    
    # Get recipients
    recipients = get_recipients()
    
    if not recipients:
        print("No recipients found in environment variable or recipients.txt file")
        return
    
    # Gmail SMTP configuration
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    
    # Send email to each recipient
    for to_email in recipients:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print(f"Email sent successfully to {to_email}")
    
    server.quit()
