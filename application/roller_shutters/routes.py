import os
from application import talisman
from flask import Blueprint, render_template, request, send_from_directory
import application.roller_shutters.controller as controller
from application.index.form import IndexForm
template_dir = os.path.abspath('../templates')
roller_shutters = Blueprint('roller_shutters', __name__, template_folder=template_dir)


@roller_shutters.route('/roller_shutters')
@talisman()
def main_roller_shutters():
    return controller.main_roller_shutters()


@roller_shutters.route('/roller_shutters/windows_doors')
@talisman()
def show_windows_doors():
    return controller.show_windows_doors()
