from flask import redirect, url_for, flash
from application.index.form import IndexForm
from application.helper.utils import send_notification


def requisition():
    form = IndexForm()
    if form.validate_on_submit():
        if len(form.number.data) < 11:
            flash("Неверно введен номер!", category='bad')
            return redirect('https://www.5master.ru/#offer')
        send_notification(form.name.data, form.number.data, form.email.data)
        flash('Спасибо за заявку! Мы перезвоним вам в ближайшее время!', category='good')
        return redirect('https://www.5master.ru/#offer')
