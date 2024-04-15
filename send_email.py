import os
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib
from email.utils import formataddr

load_dotenv()
EMAIL_SENDER = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL')


# не завершено
def send_email(name, surname, email, image, imagetype):
    email_sender, email_password, email_receiver = EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
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


# заказ
def send_order_email(surname, name, patronymic, email, phone, order_format, ornament, colour,
                     shape, size, deadline, dead_surname=None, dead_name=None, dead_patronymic=None,
                     birth_day=None, death_day=None, image=None, comment=''):
    email_sender, email_password, email_receiver = EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
    dead = 'Керамика на человека', dead_surname, dead_name, dead_patronymic + '. Годы жизни', birth_day, '-', death_day if 'текст' in order_format.lower() else ''
    subject = 'Новый заказ'
    body = f"""
    Заказчик - {surname} {name} {patronymic}, телефон: {phone}, почта: {email}.
    Формат - {order_format}.
    {'Керамика на человека', dead_surname, dead_name, dead_patronymic + '. Годы жизни', birth_day, '-', death_day
    if 'текст' in order_format.lower() else None}.
    Орнамент - {ornament}
    Цвет - {colour}
    Форма и размер - {shape, size}
    Срок изготовления до {deadline}
    {'Комментарий:', comment if comment else None}
    """

    em = EmailMessage()
    em['From'] = email_sender  # formataddr(('Тверские обряды', email_sender))
    em['To'] = email_receiver
    em['Subject'] = subject
    if 'картинка' in order_format.lower():
        if image:
            if image.content_type.split('/')[1] in ['png', 'jpg', 'jpeg']:
                em.add_attachment(image.read(), maintype='image',
                                  subtype=image.content_type.split('/')[1])
                em.set_content(body)
            else:
                em.set_content(body + '\n Ошибка с типом файла')
        else:
            em.set_content(body + '\n Ошибка с картинкой')

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


# подтверждение заказа
def send_confirm_order_email(surname, name, patronymic, email):
    email_sender, email_password, email_receiver = EMAIL_SENDER, EMAIL_PASSWORD, email
    subject = 'Ваш заказ принят'
    body = f"""
    Здравствуйте {surname} {name} {patronymic}. Ваш заказ был принял.
    """

    em = EmailMessage()
    em['From'] = formataddr(('Тверские обряды', email_sender))  # formataddr(('Тверские обряды', email_sender))
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


if __name__ == '__main__':
    send_confirm_order_email('Коротеев', 'Николай', 'Сергеевич', 'kolia9038072204@gmail.com')
