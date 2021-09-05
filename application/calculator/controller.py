from flask import render_template, redirect, url_for, request, flash
from application.calculator.form import CalculatorForm, Place, Kind, Control, Services
from application.helper.utils import send_notification_calculator


def calculator():
    form = CalculatorForm()
    # if form.validate_on_submit():
    if request.method == 'POST':
        send_notification_calculator(form.place.data, form.kind.data, form.height.data,
                                     form.width.data, form.control.data, request.form.getlist('services'),
                                     form.name.data, form.email.data, form.number.data)
        flash('Спасибо за заявку!')
        return redirect(url_for('index.index'))
    return render_template(
        'calculator.html',
        form=form,
        places=Place,
        kinds=Kind,
        controls=Control,
        services=Services
    )
