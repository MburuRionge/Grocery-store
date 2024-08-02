import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Mburu_Rionge'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False