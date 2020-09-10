from app.ext.db import db, models

def init_app(app):
    @app.cli.command()
    def create_db():
        """ This command creates the database """
        db.create_all()
