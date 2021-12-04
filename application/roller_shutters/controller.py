import os

from flask import Blueprint, render_template

from application.index.form import IndexForm

template_dir = os.path.abspath('../templates')
index_blueprint = Blueprint('index', __name__, template_folder=template_dir)


def main_roller_shutters():
    return render_template('roller_shutters/main_page.html')


def show_windows_doors():
    form = IndexForm()
    return render_template('roller_shutters/windows_doors.html', form=form)


def show_antivandal():
    form = IndexForm()
    return render_template('roller_shutters/antivandal.html', form=form)


def show_roller_gateway():
    form = IndexForm()
    return render_template('roller_shutters/roller_gateway.html', form=form)


def show_roll_with_photo():
    form = IndexForm()
    return render_template('roller_shutters/photo.html', form=form)


def show_roll_box():
    form = IndexForm()
    return render_template('roller_shutters/box.html', form=form)


def show_plumbing_shutters():
    form = IndexForm()
    return render_template('roller_shutters/plumbing_shutters.html', form=form)
