from .apps import student
from . import views


@student.route("/")
def index():
    return views.index()
