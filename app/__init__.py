from flask import Flask
from .config import Config
from .models import db, bcrypt
from .routes import init_app
from flask_migrate import Migrate  # Importando o Migrate


def init_app(app):
    from .routes import auth_bp, content_bp  # Importe os Blueprints

    app.register_blueprint(auth_bp, url_prefix='/auth')  # Prefixo para autenticação
    app.register_blueprint(content_bp)  # Sem prefixo para rotas gerais


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)

    # Inicializando o Migrate
    migrate = Migrate(app, db)
    
    from . import routes
    routes.init_app(app)

    return app
