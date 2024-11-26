from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

<<<<<<< HEAD
    from . import routes
=======
    from .import routes
>>>>>>> 537ea601e6cd2a2e3cf7d705925167402cddabbe
    routes.init_app(app)
    return app