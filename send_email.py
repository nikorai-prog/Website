import os
from email.message import EmailMessage
import ssl
import smtplib


email_sender = os.getenv('EMAIL')
email_password = os.getenv('PASSWORD')
email_receiver = os.getenv('EMAIL')


# не завершено
def send_email(receiver_email, subject, name):

    subject = 'New message'
    body = """
    Не бойся. Я проверяю как это работает."""

    em = EmailMessage()
    em['From'] = formataddr(('Тверские обряды', email_sender))  # email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


if __name__ == '__main__':
    send_email()

