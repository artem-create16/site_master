import os

from flask import Blueprint

import application.roller_shutters.controller as controller
from application import talisman

template_dir = os.path.abspath('../templates')
roller_shutters = Blueprint('roller_shutters', __name__, template_folder=template_dir)


@roller_shutters.route('/rolstavni')
@talisman()
def main_roller_shutters():
    return controller.main_roller_shutters()


@roller_shutters.route('/rolstavni/rolstavni_na_okna_dvery')
@talisman()
def show_windows_doors():
    return controller.show_windows_doors()


@roller_shutters.route('/rolstavni/antivandalnye')
@talisman()
def show_antivandal():
    return controller.show_antivandal()


@roller_shutters.route('/rolstavni/rolletnye_vorota')
@talisman()
def show_roller_gateway():
    return controller.show_roller_gateway()


@roller_shutters.route('/rolstavni/rolstavni_s_photo')
@talisman()
def show_roll_with_photo():
    return controller.show_roll_with_photo()


@roller_shutters.route('/rolstavni/rolletnye_boksy')
@talisman()
def show_roll_box():
    return controller.show_roll_box()


@roller_shutters.route('/rolstavni/rolstavni_santekhnicheskie')
@talisman()
def show_plumbing_shutters():
    return controller.show_plumbing_shutters()
