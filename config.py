import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///S1news.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123'