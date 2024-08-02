from flask import Flask
from config import ProductionConfig

def create_app(config_class=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)