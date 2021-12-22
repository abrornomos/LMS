from .apps import auth
from . import views


@auth.route("")
def index():
    views.index()
