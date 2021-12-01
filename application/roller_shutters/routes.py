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


@roller_shutters.route('/roller_shutters/antivandalnye')
@talisman()
def show_antivandal():
    return controller.show_antivandal()


@roller_shutters.route('/roller_shutters/roller_gateway')
@talisman()
def show_roller_gateway():
    return controller.show_roller_gateway()


@roller_shutters.route('/roller_shutters/roll_with_photo')
@talisman()
def show_roll_with_photo():
    return controller.show_roll_with_photo()


@roller_shutters.route('/roller_shutters/roll_box')
@talisman()
def show_roll_box():
    return controller.show_roll_box()


@roller_shutters.route('/roller_shutters/plumbing_shutters')
@talisman()
def show_plumbing_shutters():
    return controller.show_plumbing_shutters()
