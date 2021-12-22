from flask_sqlalchemy import SQLAlchemy
from manage import app


db = SQLAlchemy(app)


class Student(db.Model):

    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)


class StudentMeta(db.Model):

    __tablename__ = "student_meta"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
