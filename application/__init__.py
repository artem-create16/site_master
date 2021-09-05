import os
from flask_mail import Mail, Message
from flask import Flask
from dotenv import load_dotenv
from boto.s3.connection import S3Connection
load_dotenv()
mail = Mail()


def init_app():
    app = Flask(__name__)
    SECRET_KEY = S3Connection(os.environ['SECRET_KEY'], os.environ['SECRET_KEY'])
    MAIL_USERNAME = S3Connection(os.environ['MAIL_USERNAME'], os.environ['MAIL_USERNAME'])
    MAIL_PASSWORD = S3Connection(os.environ['MAIL_PASSWORD'], os.environ['MAIL_PASSWORD'])
    MAIL_SERVER = S3Connection(os.environ['MAIL_SERVER'], os.environ['MAIL_SERVER'])
    MAIL_PORT = S3Connection(os.environ['MAIL_PORT'], os.environ['MAIL_PORT'])
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    with app.app_context():
        from application.index.routes import index_blueprint
        from application.calculator.routes import calculator_blueprint
        app.register_blueprint(index_blueprint)
        app.register_blueprint(calculator_blueprint)

    mail.init_app(app)
    return app
