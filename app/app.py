from flask import Flask
from app.extensions import db  # Certifique-se de que você está importando o db corretamente
from app.models import User, Report # Importando os modelos



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Ajuste o caminho do banco de dados conforme necessário
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicializando o db com o app

# Criação das tabelas no contexto da aplicação, sem usar before_first_request
with app.app_context():  
    db.create_all()  # Cria as tabelas no banco de dados

if __name__ == '__main__':
    app.run(debug=True)
