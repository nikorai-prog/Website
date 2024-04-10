import os
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib

load_dotenv()
email_sender = os.getenv('EMAIL')
email_password = os.getenv('PASSWORD')
email_receiver = os.getenv('EMAIL')


# не завершено
def send_email(name, surname, email, image, imagetype):
    subject = 'Новый заказ'
    body = f"""
    Заказчик - {name} {surname}, телефон: phone_number, почта: {email}.
    Керамика на человека..."""

    em = EmailMessage()
    em['From'] = email_sender  # formataddr(('Тверские обряды', email_sender))
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    em.add_attachment(image, maintype='image',
                      subtype=imagetype)

    '''em.add_alternative("""\
    <html>
      <head></head>
      <body>
        <p>Salut!</p>
        <p>Cela ressemble à un excellent
            <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
                recipie
            </a> déjeuner.
        </p>
        <img src="cid:{asparagus_cid}" />
      </body>
    </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')'''

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


if __name__ == '__main__':
    pass
    # send_email()
