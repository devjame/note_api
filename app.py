from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from config import Config
from extensions import db
from notes.models import Notes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    @app.shell_context_processor
    def make_shell_context():
        return dict(app=create_app, db=db, Notes=Notes)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api()
