from flask_login import LoginManager
from app.ext.db.models import User

def init_app(app):
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def get_user(user_id):
        return User.query.filter_by(id=user_id).first()
