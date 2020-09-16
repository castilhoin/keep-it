from flask import render_template
from .main import bp

def page_not_found(e):
    return render_template("error.html", message="Sorry, page not found"), 404

def init_app(app):
    app.register_blueprint(bp)
    app.register_error_handler(404, page_not_found)
