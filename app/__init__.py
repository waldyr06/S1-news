from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    # Importa e registra o blueprint dos CRUDs depois que o app é criado
    from .news import news as news_blueprint
    app.register_blueprint(news_blueprint, url_prefix='/news')

    from . import routes
    routes.init_app(app)
    return app
