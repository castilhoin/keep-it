from app.ext.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

class Notebook(db.Model):
    __tablename__ = "notebooks"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String(5000), nullable=False)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
    notebook_id = db.Column(db.Integer, db.ForeignKey("notebooks.id"))
