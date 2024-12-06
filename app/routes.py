from flask import render_template

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/politics')
    def politics_page():
        return render_template('politics.html')

    @app.route('/politics/report1')
    def preport1_page():
        return render_template('preport1.html')

    @app.route('/politics/report2')
    def preport2_page():
        return render_template('preport2.html')

    @app.route('/politics/report3')
    def preport3_page():
        return render_template('preport3.html')
    
    @app.route('/esportes')
    def sports_page():
        return render_template('esportes.html')
    
    @app.route('/esportes/esporte4')
    def esporte_report4_page():
        return render_template('ereport4.html')
    
    @app.route('/esportes/esporte5')
    def esporte_report5_page():
        return render_template('ereport5.html')
    
    @app.route('/esportes/esporte6')
    def esporte_report6_page():
        return render_template('ereport6.html')

    @app.route('/cadastro')
    def Cadastro_page():
        return render_template('Cadastro.html')

    @app.route('/login')
    def login_page():
        return render_template('login.html')

    @app.route('/menu')
    def menu_page():
        return render_template('menu.html')

    @app.route('/saude')
    def healthy_page():
        return render_template('teladesaude.html')
    
    @app.route('/saude/reportsa1')
    def reportsa1_page():
        return render_template('reportsaude1.html')

    @app.route('/saude/reportsa2')
    def reportsa2_page():
        return render_template('reportsaude2.html')

    @app.route('/saude/reportsa3')
    def reportsa3_page():
        return render_template('reportsaude3.html')