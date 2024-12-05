from flask import Blueprint

# Cria o blueprint 'news' e especifica a pasta de templates
news = Blueprint('news', __name__, template_folder='templates')

# Importa as rotas do arquivo routes.py
from . import routes