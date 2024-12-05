from flask import render_template

def init_app(app):
    @app.route('/')
    def index():
        return render_template('/news/index.html')

    @app.route('/report1')
    def preport1_page():
        return render_template('preport1.html')

    @app.route('/report2')
    def preport2_page():
        return render_template('preport2.html')

    @app.route('/report3')
    def preport3_page():
        return render_template('preport3.html')
    
    @app.route('/esporte4')
    def esporte_report4_page():
        return render_template('ereport4.html')
    
    @app.route('/esporte5')
    def esporte_report5_page():
        return render_template('ereport5.html')
    
    @app.route('/esporte6')
    def esporte_report6_page():
        return render_template('ereport6.html')

    @app.route('/cadastro')
    def cadastro():
        return render_template('cadastro.html')

    @app.route('/login')
    def login_page():
        return render_template('login.html')