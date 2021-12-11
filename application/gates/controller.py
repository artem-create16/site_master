from flask import render_template

from application.index.form import IndexForm


def main_gates():
    return render_template('gates/main_page.html')


def show_gates_prom():
    form = IndexForm()
    return render_template('gates/prom.html', form=form)


def show_gates_sectionnye():
    form = IndexForm()
    return render_template('gates/sectionnye.html', form=form)


def show_gates_otkatnye():
    form = IndexForm()
    return render_template('gates/otkatnye.html', form=form)


def show_gates_raspashnye():
    form = IndexForm()
    return render_template('gates/raspashnye.html', form=form)

