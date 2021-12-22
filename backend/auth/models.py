from flask_sqlalchemy import SQLAlchemy
from manage import app


db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


class UserMeta(db.Model):

    __tablename__ = "user_meta"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
