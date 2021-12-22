from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext
from lms.settings import *
from student.apps import student
from student.models import db as student_db


app = Flask(__name__, static_url_path=STATIC_URL, static_folder=PROJECT_DIR / "static", template_folder=PROJECT_DIR / "templates")
app.config.from_pyfile("env.py")


student_db.init_app(app)
@click.argument(name="create")
def create():
    print("dddd")
    student_db.create_all()

app.cli.add_command(name=create)
app.register_blueprint(student)

# import os

# print(os.urandom(24).hex())


if __name__ == "__main__":
    app.run(debug=True)
