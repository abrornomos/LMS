from .apps import attendance
from . import views


@attendance.route("")
def index():
    views.index()
