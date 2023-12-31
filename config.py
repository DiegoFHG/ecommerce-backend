import psycogreen.gevent
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Patch PostgreSQL driver for Gunicorn gevent (async)
psycogreen.gevent.patch_psycopg()

app = Flask('ecommerce')

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://ecommerce:ecommerce@ecommerce-db:5432/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
CORS(app)