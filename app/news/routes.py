from flask import render_template

@news.route('/') # Protege a rota, exigindo que o usuário esteja autenticado
def index(): 
    return render_template('news/index.html')