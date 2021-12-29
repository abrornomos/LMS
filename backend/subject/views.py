from flask import jsonify

from .models import *


def get_subjects():
    subjects = [ subject.format() for subject in Subject.query.all() ]
    return jsonify(subjects)
