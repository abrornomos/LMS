from .apps import subject
from . import views


@subject.route("/")
def get_subjects():
    return views.get_subjects()
