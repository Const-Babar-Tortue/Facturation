from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# API
from .api.signup.signup import Signup
from .api.bills import bill_route

app = Flask(__name__, instance_relative_config=False)
api = Api(app)


def init_app():
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        db.create_all()

        from Application.api.jwt.jwt import authenticate, identity
        JWT(app, authenticate, identity)

    api.add_resource(Signup, '/signup')

    return app
