import os

from flask_mail import Message

from application import mail


def send_notification(name, number, email):
    msg = Message(
        'Новая заявка ',
        sender=os.environ['WORK_MAIL'],
        recipients=[os.environ['ADMIN_EMAIL']]
    )
    msg.body = f"Имя: {name}\nНомер: {number}\nПочта: {email}"
    mail.send(msg)
