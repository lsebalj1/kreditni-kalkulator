from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def _create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kreditni_kalkulator.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
