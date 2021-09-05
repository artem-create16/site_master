import os
from flask_mail import Mail, Message
from flask import Flask
from dotenv import load_dotenv
from boto.s3.connection import S3Connection
load_dotenv()
mail = Mail()


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = str(os.getenv("WORK_MAIL"))
    app.config['MAIL_PASSWORD'] = str(os.getenv("WORK_MAIL_PASSWORD"))
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    with app.app_context():
        from application.index.routes import index_blueprint
        from application.calculator.routes import calculator_blueprint
        app.register_blueprint(index_blueprint)
        app.register_blueprint(calculator_blueprint)

    mail.init_app(app)
    return app
