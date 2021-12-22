from .apps import group
from . import views


@group.route("")
def index():
    views.index()
