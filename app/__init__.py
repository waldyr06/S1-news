<<<<<<< HEAD
=======
from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

    from .import routes
    routes.init_app(app)
    return app
>>>>>>> d955c7e55dbd23a6cb4aba9e2270fd1da3c08f37
