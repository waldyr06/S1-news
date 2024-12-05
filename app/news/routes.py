from flask import render_template
from . import news

@news.route('/') # Protege a rota, exigindo que o usuário esteja autenticado
def index(): 
    return render_template('news/index.html')

@news.route('/politics') # Protege a rota, exigindo que o usuário esteja autenticado
def politics(): 
    return render_template('news/politics.html')