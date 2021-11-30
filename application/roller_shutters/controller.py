import os
from application import talisman
from flask import Blueprint, render_template, request, send_from_directory
import application.index.controller as controller
from application.index.form import IndexForm
template_dir = os.path.abspath('../templates')
index_blueprint = Blueprint('index', __name__, template_folder=template_dir)


def main_roller_shutters():
    return render_template('roller_shutters/main_page.html')


def show_windows_doors():
    form = IndexForm()
    return render_template('roller_shutters/windows_doors.html', form=form)
