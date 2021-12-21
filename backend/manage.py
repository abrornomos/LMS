from click.decorators import command
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import AppGroup
from lms.settings import *
from student.apps import student
from student.models import db

def create_app(config_filename):
    app = Flask(__name__, static_url_path=STATIC_URL, static_folder=PROJECT_DIR / "static", template_folder=PROJECT_DIR / "templates")
    app.config.from_pyfile(config_filename)
    
    db.init_app(app)
    with app.app_context():
        # @app.cli.command("db")
        # @click.argument("comand")
        # def create_db(comand):
        #     print("dddd")
        #     if comand == 'create':
        #         db.create_all()
        #     elif comand == 'drop':
        #         db.drop_all()
        #     elif comand == 'reset':
        #         db.drop_all()
        #         db.create_all()
        db.create_all()
    

    app.register_blueprint(student)
   
    return app

# import os

# print(os.urandom(24).hex())


if __name__ == "__main__":
    app = create_app('env.py')

    
    app.run(debug=True)
