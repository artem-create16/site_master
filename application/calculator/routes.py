import os

from flask import Blueprint, render_template, request, send_from_directory
import application.calculator.controller as controller
template_dir = os.path.abspath('../templates')
calculator_blueprint = Blueprint('calculator', __name__, template_folder=template_dir)


@calculator_blueprint.route('/calculator', methods=["POST", "GET"])
def calculator():
    return controller.calculator()
