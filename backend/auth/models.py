from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    fullname = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), unique=True, nullable=False)
    last_login = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime)

    metas = relationship("UserMeta", backref="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def format(self):
        return {
            'username': self.username,
            'fullname': self.fullname,
            'role': self.role,
            'last_login': self.last_login,
            'created_time': self.created_time,
            'attributes': [{
                'key': meta.format()['key'],
                'value': meta.format()['value'],
            } for meta in self.metas]
        }


class UserMeta(db.Model):

    __tablename__ = "user_meta"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    key = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.String(200), unique=True, nullable=False)

    def format(self):
        return {
            'user_id': self.user_id,
            'key': self.key,
            'value': self.value
        }
