# routes.py

from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db  # Importando db de extensions.py
from models import User, Report

def init_app(app):
    # Rota inicial
    @app.route('/')
    def home():
        return render_template('index.html')

    # Página de Política
    @app.route('/politics')
    def politics_page():
        return render_template('politics.html')

    # Relatórios de Política
    @app.route('/politics/report1')
    def preport1_page():
        return render_template('preport1.html')

    @app.route('/politics/report2')
    def preport2_page():
        return render_template('preport2.html')

    @app.route('/politics/report3')
    def preport3_page():
        return render_template('preport3.html')

    # Página de Esportes
    @app.route('/esportes')
    def esportes_page():
        return render_template('esportes.html')

    # Relatórios de Esporte
    @app.route('/noticia/esporte4')
    def esporte_report4_page():
        return render_template('ereport4.html')

    @app.route('/noticia/esporte5')
    def esporte_report5_page():
        return render_template('ereport5.html')

    @app.route('/noticia/esporte6')
    def esporte_report6_page():
        return render_template('ereport6.html')

    # Página de Cadastro
    @app.route('/Cadastro.html')
    def Cadastro_page():
        return render_template('Cadastro.html')

    # Página de Login
    @app.route('/login.html')
    def login_page():
        return render_template('login.html')

    # Rota para o formulário de cadastro
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            nome_completo = request.form['nome_completo']  # Corrigido para 'nome_completo'
            email = request.form['email']
            senha = request.form['senha']

            # Criar um novo usuário
            user = User(nome_completo=nome_completo, email=email)
            user.set_password(senha)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('home'))

        return render_template('register.html')

    # Rota para o formulário de login
    @app.route('/login', methods=['POST'])
    def login():
        email = request.form['email']
        senha = request.form['senha']

        user = User.query.filter_by(email=email).first()  # Buscar usuário pelo email

        if user and check_password_hash(user.senha, senha):  # Verificar senha
            return redirect(url_for('home'))  # Redirecionar para a página inicial
        else:
            return 'Falha no login, tente novamente.'
