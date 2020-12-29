from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from config import Config
from extensions import db
from notes.models import Notes
from notes.resources.note import NoteResource, NoteListResource


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
    # ma.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(NoteListResource, '/notes')
    api.add_resource(NoteResource, '/note/<int:note_id>')


if __name__ == '__main__':
    app = create_app()
    app.run()
