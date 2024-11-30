from flask import render_template

def init_app(app):
    @app.route('/')
    def home():
        return render_template('esportes.html')

    @app.route('/report1')
    def report1_page():
        return render_template('report1.html')

    @app.route('/report2')
    def report2_page():
        return render_template('report2.html')

    @app.route('/report3')
    def report3_page():
        return render_template('report3.html')