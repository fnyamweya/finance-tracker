import os

class Config:
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///finance.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
