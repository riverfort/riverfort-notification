import os
import smtplib
from email.message import EmailMessage
from typing import List

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")


def send_email(subject: str, contacts: List[str], content: str, html: str):
    for contact in contacts:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = contact

        msg.set_content(content)
        msg.add_alternative(
            html,
            subtype="html",
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg=msg)
            print(f"INFO: sent email to {contact}")
