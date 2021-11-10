import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

contacts = [EMAIL_ADDRESS, "qyang.nie@gmail.com"]


def send_email(html):
    for contact in contacts:
        msg = EmailMessage()
        msg["Subject"] = "Top Gainers: London"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = contact

        msg.set_content("This is a plain text email: Hello World")
        msg.add_alternative(
            html,
            subtype="html",
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg=msg)
