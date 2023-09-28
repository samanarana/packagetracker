from flask import Flask
import os
from .main import bp
from flask_migrate import Migrate
from .models import db


app = Flask(__name__)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

app.config.from_object(Config)

app.register_blueprint(bp)

db.init_app(app)

migrate = Migrate(app, db)
