from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import db, User
from flask_login import LoginManager, login_user

auth_bp = Blueprint('auth', __name__)
content_bp = Blueprint('content', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['senha']

        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado.', 'error')
            return redirect(url_for('auth.register'))

        user = User(name=name, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('content.indexlog'))

        flash('Credenciais inválidas. Tente novamente.', 'error')
        return redirect(url_for('auth.login'))

    return render_template('login.html')

@content_bp.route('/')
def index():
    return render_template('index.html')

@content_bp.route('/inicio')
def indexlog():
    return render_template('indexlog.html')

@content_bp.route('/Política')
def policy_page():
    return render_template('policy.html')

@content_bp.route('/Política/aumento-do-salario-minimo-e-aprovado')
def preport1_page():
    return render_template('policyR1.html')

@content_bp.route('/Política/protestos-em-brasilia')
def preport2_page():
    return render_template('policyR2.html')

@content_bp.route('/Política/eleicoes-2024-cabo-de-santo-agostinho')
def preport3_page():
    return render_template('policyR3.html')

@content_bp.route('/Esportes')
def sport_page():
    return render_template('sport.html')

@content_bp.route('/Esportes/botafogo-campeao')
def esporte_report4_page():
    return render_template('sportR1.html')

@content_bp.route('/Esportes/corinthians-libertadores')
def esporte_report5_page():
    return render_template('sportR2.html')

@content_bp.route('/Esportes/sport-club-recife-serie-a')
def esporte_report6_page():
    return render_template('sportR3.html')

@content_bp.route('/Home')
def menu_page():
    return render_template('menu.html')

@content_bp.route('/Saude')
def health_page():
    return render_template('health.html')

@content_bp.route('/Saude/impactos-apostas-sobre-saude-mental')
def reportsa1_page():
    return render_template('healthR1.html')

@content_bp.route('/Saude/queimadas-e-secas')
def reportsa2_page():
    return render_template('healthR2.html')

@content_bp.route('/Saude/cursos-de-estetica-atividades-de-risco')
def reportsa3_page():
    return render_template('healthR3.html')


def init_app(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(content_bp)
    login_manager.init_app(app)
