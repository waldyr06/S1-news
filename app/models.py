from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # Importando o Bcrypt
from flask_login import UserMixin  # Importe o UserMixin do flask_login

# Inicializando as instâncias do Flask e do SQLAlchemy
db = SQLAlchemy()
bcrypt = Bcrypt()  # Inicializando o Bcrypt

# Model do Usuário
class User(db.Model, UserMixin):  # Herda UserMixin aqui
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    # Esses métodos são herdados automaticamente do UserMixin, mas vou mostrar como eles são:
    def is_authenticated(self):
        return True  # Indica que o usuário está autenticado

    def is_active(self):
        return True  # Indica que o usuário está ativo

    def is_anonymous(self):
        return False  # Indica que o usuário não é anônimo

