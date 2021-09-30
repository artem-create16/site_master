from flask import redirect, url_for, flash
from application.index.form import IndexForm
from application.helper.utils import send_notification


def requisition():
    form = IndexForm()
    if form.validate_on_submit():
        send_notification(form.name.data, form.number.data, form.email.data)
        flash('Спасибо за заявку!')
        return redirect(url_for('index.index'))
