from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import db, User
from flask_login import LoginManager, login_user

# Configuração do Blueprint para autenticação
auth_bp = Blueprint('auth', __name__)
content_bp = Blueprint('content', __name__)  # Blueprint para rotas de conteúdo

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Rotas de autenticação
from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import db, User

auth_bp = Blueprint('auth', __name__)  # Blueprint de autenticação

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['senha']

        # Verificar se o email já está cadastrado
        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado.', 'error')
            return redirect(url_for('auth.register'))

        # Criar e salvar o novo usuário
        user = User(name=name, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))  # Redirecionar para login após o registro

    return render_template('register.html')  # Render



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('content.index'))

        flash('Credenciais inválidas.', 'error')
        return redirect(url_for('auth.login'))

    return render_template('login.html')


# Rotas de conteúdo geral
@content_bp.route('/')
def index():
    return render_template('index.html')

@content_bp.route('/politics')
def policy_page():
    return render_template('policy.html')

@content_bp.route('/politics/report1')
def preport1_page():
    return render_template('policyR1.html')

@content_bp.route('/politics/report2')
def preport2_page():
    return render_template('policyR2.html')

@content_bp.route('/politics/report3')
def preport3_page():
    return render_template('policyR3.html')

@content_bp.route('/esportes')
def sport_page():
    return render_template('sport.html')

@content_bp.route('/esportes/esporte4')
def esporte_report4_page():
    return render_template('sportR1.html')

@content_bp.route('/esportes/esporte5')
def esporte_report5_page():
    return render_template('sportR2.html')

@content_bp.route('/esportes/esporte6')
def esporte_report6_page():
    return render_template('sportR3.html')

@content_bp.route('/menu')
def menu_page():
    return render_template('menu.html')

@content_bp.route('/saude')
def health_page():
    return render_template('health.html')

@content_bp.route('/saude/reportsa1')
def reportsa1_page():
    return render_template('healthR1.html')

@content_bp.route('/saude/reportsa2')
def reportsa2_page():
    return render_template('healthR2.html')

@content_bp.route('/saude/reportsa3')
def reportsa3_page():
    return render_template('healthR3.html')


# Função init_app para inicializar Blueprints
def init_app(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(content_bp)
    login_manager.init_app(app)
