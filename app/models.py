from . import db
import datetime

# Definindo o modelo
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    descricao = db.Column(db.Text, nullable=False)
    reporter = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Report {self.titulo}>"