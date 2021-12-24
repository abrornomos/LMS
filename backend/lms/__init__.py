from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from lms.settings import *
from student.apps import student


def create_app():
    app = Flask(__name__, static_url_path=STATIC_URL, static_folder=PROJECT_DIR / "static", template_folder=PROJECT_DIR / "templates")
    app.config.from_pyfile("env.py")
    app.register_blueprint(student)

    return app


app = create_app()
db = SQLAlchemy(app)

from . import urls
