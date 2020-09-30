import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# TODO https://pythonru.com/uroki/19-struktura-i-jeskiz-prilozhenija-flask
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')

# extensions initializer
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# import views
from . import views
