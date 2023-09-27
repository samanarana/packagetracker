from flask import Flask
import os
from .main import bp

app = Flask(__name__)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

app.config.from_object(Config)

app.register_blueprint(bp)
