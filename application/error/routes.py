from flask import render_template, Blueprint
import os
from smtplib import SMTPAuthenticationError


template_dir = os.path.abspath('../templates')
error_blueprint = Blueprint('error', __name__, url_prefix='/error', template_folder=template_dir)


@error_blueprint.app_errorhandler(404)
def status_code_404(error):
    return render_template('errors/error404.html'), 404


@error_blueprint.app_errorhandler(500)
def status_code_500(error):
    return render_template('errors/error500.html'), 500


@error_blueprint.app_errorhandler(SMTPAuthenticationError)
def status_code_535(error):
    return render_template('errors/error535.html'), 535
