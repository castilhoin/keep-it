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

@bp.route("/<int:notebook>", methods=["GET"])
def list_notes(notebook):
    if current_user.is_authenticated:
        notebooks = Notebook.query.filter_by(user_id=current_user.id)
        current_notebook = Notebook.query.filter_by(id=notebook).first()
        if current_notebook.user_id == current_user.id:
            notes = Note.query.filter_by(notebook_id=notebook)
            return render_template("note/list.html", notebooks=notebooks, current_notebook=current_notebook, notes=notes)
        return render_template("error.html", notebooks=notebooks, message="Sorry, you don't have permission to access this resource.")
    else:
        return redirect(url_for("site.login"))

@bp.route("/notebook/new", methods=["GET", "POST"])
def new_notebook():
    if current_user.is_authenticated:
        notebooks = Notebook.query.filter_by(user_id=current_user.id)
        if request.method == "POST":
            name = request.form["name"]
            if not name:
                return render_template("error.html", notebooks=notebooks, message="Please, insert a name for your notebook")
            color = request.form["color"]
            if not color:
                return render_template("error.html", notebooks=notebooks, message="Please, choose a color for your notebook")
            new_notebook = Notebook(name, color, current_user.id)
            db.session.add(new_notebook)
            db.session.commit()
            return redirect(url_for("site.index"))
        else:
            return render_template("notebook/new.html", notebooks=notebooks)
    else:
        return redirect(url_for("site.login"))

@bp.route("/<int:notebook>/edit", methods=["GET", "POST"])
def edit_notebook(notebook):
    if current_user.is_authenticated:
        notebooks = Notebook.query.filter_by(user_id=current_user.id)
        current_notebook = Notebook.query.filter_by(id=notebook).first()
        if request.method == "POST":
            name = request.form["name"]
            if not name:
                return render_template("error.html", notebooks=notebooks, message="Please, insert a name for your notebook")
            color = request.form["color"]
            if not color:
                return render_template("error.html", notebooks=notebooks, message="Please, choose a color for your notebook")
            if current_notebook.user_id == current_user.id:
                edited_notebook = Notebook.query.filter_by(id=notebook).first()
                edited_notebook.name = name
                edited_notebook.color = color
                db.session.commit()
                return redirect(url_for("site.list_notes", notebook=notebook))
            return render_template("error.html", notebooks=notebooks, message="Sorry, you don't have permission to access this resource.")
        else:
            return render_template("notebook/edit.html", notebooks=notebooks, current_notebook=current_notebook)
    else:
        return redirect(url_for("site.login"))
