from flask import Flask, render_template

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/politics')
    def politics():
        return render_template('politics.html')