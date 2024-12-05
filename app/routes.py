from flask import render_template

def init_app(app):
    @app.route('/main')
    def menu_page():
        return render_template('menu.html')
    @app.route('/saude')
    def healthy_page():
        return render_template('teladesaude.html')
    
    @app.route('/reportsa1')
    def reportsa1_page():
        return render_template('reportsaude1.html')

    @app.route('/reportsa2')
    def reportsa2_page():
        return render_template('reportsaude2.html')

    @app.route('/reportsa3')
    def reportsa3_page():
        return render_template('reportsaude3.html')
   
