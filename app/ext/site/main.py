from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/", methods=["GET"])
def index():
    return "Hello!"