from flask import Flask

from lms.settings import *
from student.apps import student
from student.models import db as student_db


app = Flask(__name__, static_url_path=STATIC_URL, static_folder=PROJECT_DIR / "static", template_folder=PROJECT_DIR / "templates")
app.config.from_pyfile("env.py")


app.register_blueprint(student)


student_db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
