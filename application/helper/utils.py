import os
import pytz
from flask_mail import Message
from application import mail
from datetime import datetime


def send_notification(name, number, email):
    timezone = pytz.timezone("Europe/Moscow")
    date = datetime.now(timezone).strftime('%d.%m.%y %H:%M:%S')
    msg = Message(
        f'Новая заявка ({date})',
        sender=os.environ['WORK_MAIL'],
        recipients=[os.environ['ADMIN_EMAIL']]
    )
    msg.body = f"Дата: {date}\nИмя: {name}\nНомер: {number}\nПочта: {email}"
    mail.send(msg)


def send_notification_calculator(place, kind, height, width, control, services, name, email, number):
    date = datetime.now().strftime('%d.%m.%y %H:%M:%S')
    msg = Message(
        f'Новая заявка ({date})',
        sender=os.environ['WORK_MAIL'],
        recipients=[os.environ['ADMIN_EMAIL']]
    )
    msg.body = f"Дата: {date}\nИмя: {name}\nНомер: {number}\nПочта: {email}\n" \
               f"Место установки: {place}\nВид рольставни: {kind}\nВысота: {height}\nШирина: {width}\n" \
               f"Управление: {control}\nУслуги: {services}"
    mail.send(msg)
