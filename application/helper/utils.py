import os

from flask_mail import Message
from boto.s3.connection import S3Connection
from application import mail


def send_notification(name, number, email):
    msg = Message(
        'Новая заявка ',
        sender=S3Connection(os.environ['WORK_MAIL'], os.environ['WORK_MAIL']),
        recipients=S3Connection(os.environ['ADMIN_EMAIL'], os.environ['ADMIN_EMAIL'])
    )
    msg.body = f"Имя: {name}\nНомер: {number}\nПочта: {email}"
    mail.send(msg)
