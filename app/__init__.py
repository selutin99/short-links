import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')

# extensions initializer
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# initialize imports
from app import models
from app import swagger

from app import routes
