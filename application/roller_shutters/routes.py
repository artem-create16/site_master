import os

from flask import Blueprint

import application.roller_shutters.controller as controller
from application import talisman
from application.helper.utils import requisition as helper_requisition


template_dir = os.path.abspath('../templates')
roller_shutters = Blueprint('roller_shutters', __name__, template_folder=template_dir)


@roller_shutters.route('/rolstavni')
@talisman()
def main_roller_shutters():
    return controller.main_roller_shutters()


@roller_shutters.route('/rolstavni/rolstavni-na-okna-dvery')
@talisman()
def show_windows_doors():
    return controller.show_windows_doors()


@roller_shutters.route('/rolstavni/rolstavni-na-okna-dvery', methods=["POST", "GET"])
def requisition_okna(*args):
    return helper_requisition(redirect_url='roller_shutters.show_windows_doors', link='rolstavni-na-okna-dvery', *args)


@roller_shutters.route('/rolstavni/antivandalnye')
@talisman()
def show_antivandal():
    return controller.show_antivandal()


@roller_shutters.route('/rolstavni/antivandalnye', methods=["POST", "GET"])
def requisition_antivandalnye(*args):
    return helper_requisition(redirect_url='roller_shutters.show_antivandal', link='rolstavni/antivandalnye', *args)


@roller_shutters.route('/rolstavni/rolletnye-vorota')
@talisman()
def show_roller_gateway():
    return controller.show_roller_gateway()


@roller_shutters.route('/rolstavni/rolletnye-vorota', methods=["POST", "GET"])
def requisition_rolletnye_vorota(*args):
    return helper_requisition(redirect_url='roller_shutters.show_roller_gateway', link='rolletnye-vorota', *args)


@roller_shutters.route('/rolstavni/rolstavni-s-photo')
@talisman()
def show_roll_with_photo():
    return controller.show_roll_with_photo()


@roller_shutters.route('/rolstavni/rolstavni-s-photo', methods=["POST", "GET"])
def requisition_photo(*args):
    return helper_requisition(redirect_url='roller_shutters.show_roll_with_photo', link='rolstavni-s-photo', *args)


@roller_shutters.route('/rolstavni/rolletnye-boksy')
@talisman()
def show_roll_box():
    return controller.show_roll_box()


@roller_shutters.route('/rolstavni/rolletnye-boksy', methods=["POST", "GET"])
def requisition_box(*args):
    return helper_requisition(redirect_url='roller_shutters.show_roll_box', link='rolletnye-boksy', *args)


@roller_shutters.route('/rolstavni/rolstavni-santekhnicheskie')
@talisman()
def show_plumbing_shutters():
    return controller.show_plumbing_shutters()


@roller_shutters.route('/rolstavni/rolstavni-santekhnicheskie', methods=["POST", "GET"])
def requisition_santekhnicheskie(*args):
    return helper_requisition(redirect_url='roller_shutters.show_plumbing_shutters', link='rolstavni-santekhnicheskie', *args)
