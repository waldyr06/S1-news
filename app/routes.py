from flask import render_template

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/politics')
    def policy_page():
        return render_template('policy.html')

    @app.route('/politics/report1')
    def preport1_page():
        return render_template('policyR1.html')

    @app.route('/politics/report2')
    def preport2_page():
        return render_template('policyR2.html')

    @app.route('/politics/report3')
    def preport3_page():
        return render_template('policyR3.html')
    
    @app.route('/esportes')
    def sport_page():
        return render_template('sport.html')
    
    @app.route('/esportes/esporte4')
    def esporte_report4_page():
        return render_template('sportR1.html')
    
    @app.route('/esportes/esporte5')
    def esporte_report5_page():
        return render_template('sportR2.html')
    
    @app.route('/esportes/esporte6')
    def esporte_report6_page():
        return render_template('sportR3.html')

    @app.route('/cadastro')
    def Cadastro_page():
        return render_template('register.html')

    @app.route('/login')
    def login_page():
        return render_template('login.html')

    @app.route('/menu')
    def menu_page():
        return render_template('menu.html')

    @app.route('/saude')
    def health_page():
        return render_template('health.html')
    
    @app.route('/saude/reportsa1')
    def reportsa1_page():
        return render_template('healthR1.html')

    @app.route('/saude/reportsa2')
    def reportsa2_page():
        return render_template('healthR2.html')

    @app.route('/saude/reportsa3')
    def reportsa3_page():
        return render_template('healthR3.html')