from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.ext.db import db
from app.ext.db.models import User, Notebook, Note

bp = Blueprint("site", __name__)

@bp.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        notebooks = Notebook.query.filter_by(user_id=current_user.id)
        return render_template("index.html", notebooks=notebooks)
    else:
        return redirect(url_for("site.login"))

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("site.index"))
    else:
        if request.method == "POST":
            name = request.form["name"]
            if not name:
                return render_template("error.html", message="Please, insert a name")
            email = request.form["email"]
            if not email:
                return render_template("error.html", message="Please, insert an email")
            password = request.form["password"]
            if not password:
                return render_template("error.html", message="Please, insert a password")
            user = User(name, email, password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("site.login"))
        else:
            return render_template("signup.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("site.index"))
    else:
        if request.method == "POST":
            email = request.form["email"]
            if not email:
                return render_template("error.html", message="Please, insert your email")
            password = request.form["password"]
            if not password:
                return render_template("error.html", message="Please, insert your password")
            user = User.query.filter_by(email=email).first()
            if not user:
                return render_template("error.html", message="User does not exist")
            if not user.verify_password(password):
                return render_template("error.html", message="Incorrect password")
            login_user(user)
            return redirect(url_for("site.index"))
        else:
            return render_template("login.html")

@bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("site.login"))
