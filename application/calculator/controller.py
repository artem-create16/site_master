from flask import render_template, redirect, url_for, request, flash
from application.calculator.form import CalculatorForm, Place, Kind, Control, Services


def calculator():
    form = CalculatorForm()
    if request.method == "POST":
    # if form.validate_on_submit():
        print(form.place.data)
        return redirect(url_for('index.index'))
    return render_template('test.html', form=form,
                           places=Place,
                           kinds=Kind,
                           controls=Control,
                           services=Services)
