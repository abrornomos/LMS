from lms import db


class Student(db.Model):

    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)


class StudentMeta(db.Model):

    __tablename__ = "student_meta"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    key = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.String(200), unique=True, nullable=False)
