from flask_script import Command
from sqlalchemy_utils import database_exists, create_database, drop_database

from app import app


class DatabaseInitializeCommand(Command):
    def run(self):
        reset_db()


def reset_db():
    if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        drop_database(app.config['SQLALCHEMY_DATABASE_URI'])

    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
