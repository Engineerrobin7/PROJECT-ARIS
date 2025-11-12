# api/email_api.py
"""
Email integration for sending and checking emails.
"""
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('config', 'config.env'))

class EmailAPI:
    def __init__(self):
        self.email_address = os.getenv("EMAIL_ADDRESS", "")
        self.email_password = os.getenv("EMAIL_PASSWORD", "")
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.imap_server = os.getenv("IMAP_SERVER", "imap.gmail.com")
    
    def send_email(self, to_address, subject, body):
        """
        Send an email.
        
        Args:
            to_address (str): Recipient email address
            subject (str): Email subject
            body (str): Email body
        """
        if not self.email_address or not self.email_password:
            return "Email not configured. Please add EMAIL_ADDRESS and EMAIL_PASSWORD to config.env"
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = to_address
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
            server.quit()
            
            return f"Email sent to {to_address}."
        except Exception as e:
            return f"Error sending email: {str(e)}"
    
    def check_unread_emails(self, max_count=5):
        """Check for unread emails."""
        if not self.email_address or not self.email_password:
            return "Email not configured."
        
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.email_address, self.email_password)
            mail.select('inbox')
            
            status, messages = mail.search(None, 'UNSEEN')
            email_ids = messages[0].split()
            
            if not email_ids:
                return "No unread emails."
            
            unread_count = len(email_ids)
            summaries = []
            
            for email_id in email_ids[-max_count:]:
                status, msg_data = mail.fetch(email_id, '(RFC822)')
                msg = email.message_from_bytes(msg_data[0][1])
                
                subject = msg.get('Subject', 'No Subject')
                from_addr = msg.get('From', 'Unknown')
                summaries.append(f"From {from_addr}: {subject}")
            
            mail.close()
            mail.logout()
            
            return f"You have {unread_count} unread emails. " + ". ".join(summaries)
        except Exception as e:
            return f"Error checking emails: {str(e)}"
