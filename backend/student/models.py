from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)


class StudentMeta(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
