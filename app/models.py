from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # Importando o Bcrypt

# Inicializando as instâncias do Flask e do SQLAlchemy
db = SQLAlchemy()
bcrypt = Bcrypt()  # Inicializando o Bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')  # Usando bcrypt para gerar o hash da senha

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)  # Verificando a senha com bcrypt
