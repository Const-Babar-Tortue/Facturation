from flask import Flask
from flask_jwt import JWT
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()

# API
from .api.register.register import Register
from .api.bills import bill_route

app = Flask(__name__, instance_relative_config=False)
api = Api(app)
CORS(app)


def init_app():
    app.config.from_object("config.Config")

    logging.getLogger('flask_cors').level = logging.DEBUG

    db.init_app(app)

    with app.app_context():
        db.create_all()

        from Application.api.jwt.jwt import authenticate, identity
        JWT(app, authenticate, identity)

    api.add_resource(Register, '/register')

    return app
