import os

from flask_mail import Message
from application import mail
from datetime import datetime


def send_notification(name, number, email):
    date = datetime.now().strftime('%d.%m.%y %H:%M:%S')
    msg = Message(
        f'Новая заявка ({date})',
        sender=os.environ['WORK_MAIL'],
        recipients=[os.environ['ADMIN_EMAIL']]
    )
    msg.body = f"Дата: {date}\nИмя: {name}\nНомер: {number}\nПочта: {email}"
    mail.send(msg)

