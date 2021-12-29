from flask import Flask

from lms.settings import *
from student import student
from subject import subject
from subject.models import db as subject_db


def create_app():
    app = Flask(__name__, static_url_path=STATIC_URL, static_folder=PROJECT_DIR / "static", template_folder=PROJECT_DIR / "templates")
    app.config.from_pyfile("env.py")
    app.register_blueprint(student)
    app.register_blueprint(subject)
    subject_db.init_app(app)
    @app.after_request
    def after_request(response):
        header = response.headers
        header.add('Access-Control-Allow-Origin', '*')
        header.add('Access-Control-Allow-Headers', '*')
        header.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response
    with app.app_context():
        subject_db.create_all()

    return app


app = create_app()

from . import urls
