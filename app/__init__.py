from flask import Flask
from app.ext import config
from app.ext import db
from app.ext import login
from app.ext import cli
from app.ext import site

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    login.init_app(app)
    cli.init_app(app)
    site.init_app(app)
    return app
