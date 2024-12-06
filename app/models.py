from flask_sqlalchemy import SQLAlchemy
from datetime import date, time

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.DateTime, default=db.func.current_timestamp())  

    def __repr__(self):
        return f'<Usuário {self.name}>'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return f'<Post {self.title}>'

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    teams = db.relationship("Team", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    team_shield = db.Column(db.String(200), nullable=False)
    social_media = db.Column(db.String(300), nullable=False)
    state = db.Column(db.String(70), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    description = db.Column(db.String(500), nullable=True)

    user = db.relationship('User', backref=db.backref('teams', lazy=True))
    category = db.relationship("Category", back_populates="teams")

    def __repr__(self):
        return f"<Team(id={self.id}, name='{self.name}')>"

class Referee(db.Model):
    __tablename__ = 'referee'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    user = db.relationship('User', backref=db.backref('referees', lazy=True))

    def __repr__(self):
        return f'<Referee {self.name}>'

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(200), unique=True, nullable=False)
    district = db.Column(db.String(200), unique=True, nullable=False)
    city = db.Column(db.String(200), unique=True, nullable=False)
    state = db.Column(db.String(200), unique=True, nullable=False)
    zip = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('addresses', lazy=True))

    def __repr__(self):
        return f"<Address(id={self.id}, street='{self.street}')>"

class Scheduling(db.Model):
    __tablename__ = 'scheduling'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    local = db.Column(db.String(100), unique=True, nullable=False)
    time = db.Column(db.Time, nullable=False)
    price = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('schedules', lazy=True))
    
    def __repr__(self):    
        return f"<Scheduling(id={self.id}, time={self.time}, date={self.date})>"

class Stats(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    matches = db.Column(db.Integer, nullable=False)
    victories = db.Column(db.Integer, nullable=False)
    ties = db.Column(db.Integer, nullable=False)
    defeats = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    yellow_cards = db.Column(db.Integer, nullable=False)
    red_cards = db.Column(db.Integer, nullable=False)
    motm = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('stats', lazy=True))
    
    def __repr__(self):    
        return f"<Stats(id={self.id})>"

class TeamStats(db.Model):
    __tablename__ = 'team_stats'

    id = db.Column(db.Integer, primary_key=True)
    matches = db.Column(db.Integer, nullable=False)
    victories = db.Column(db.Integer, nullable=False)
    ties = db.Column(db.Integer, nullable=False)
    defeats = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    yellow_cards = db.Column(db.Integer, nullable=False)
    red_cards = db.Column(db.Integer, nullable=False)
    highest_scorer = db.Column(db.String(200), nullable=False)
    highest_assister = db.Column(db.String(200), nullable=False)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team', backref=db.backref('team_stats', lazy=True))

    def __repr__(self):    
        return f"<TeamStats(id={self.id})>"
