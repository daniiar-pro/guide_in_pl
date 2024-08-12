import re
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


class Report:
    load_dotenv()
    
    service_email = os.getenv("SERVICE_EMAIL")
    service_password = os.getenv("SERVICE_PASSWORD")
    to_email = "youremail@gmail.com"  #Enter your email

    @staticmethod
    def validate_email(email):
        """Validate user's email"""
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    @classmethod
    def report_issue(cls):
        """Report an issue related to site maintenance"""
        from_email = input("Your Email: ")


        if not cls.validate_email(from_email):
            print("Invalid email format")
            return

        message = input("Please enter the report message: ")


        msg = EmailMessage()
        msg["Subject"] = "Report an Issue"
        msg["From"] = from_email
        msg["To"] = cls.to_email
        msg.set_content(f"Message from {from_email}:\n\n{message}")

        try:

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(cls.service_email, cls.service_password)
                smtp.send_message(msg)
                print(f"Email sent to {cls.to_email}\n")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}\n")


report = Report.report_issue
