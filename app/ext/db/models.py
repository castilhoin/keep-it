from app.ext.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

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

    def __init__(self, name, color, user_id):
        self.name = name
        self.color = color
        self.user_id = user_id

class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String(5000), nullable=False)
    modified_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    notebook_id = db.Column(db.Integer, db.ForeignKey("notebooks.id"))

    def __init__(self, content, modified_at, user_id, notebook_id):
        self.content = content
        self.modified_at = modified_at
        self.user_id = user_id
        self.notebook_id = notebook_id
