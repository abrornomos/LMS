from .apps import student
from . import views

@student.route("")
def index():
    views.index()
