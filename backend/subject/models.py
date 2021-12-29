from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Subject(db.Model):

    __tablename__ = "subject"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def format(self):
        return {
            'name': self.name,
        }
