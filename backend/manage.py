from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from lms.settings import *
from student.apps import student


app = Flask(__name__, static_url_path=STATIC_URL, static_folder=PROJECT_DIR / "static", template_folder=PROJECT_DIR / "templates")

config = Config()
app.config.from_object(config)

db = SQLAlchemy(app)


app.register_blueprint(student)


if __name__ == "__main__":
    app.run(debug=True)
