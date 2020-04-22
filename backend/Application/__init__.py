from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# API
from .api.register import Register
from .api.clients import Clients
from .api.getNameClient import GetNameClient
from .api.deleteClient import DeleteClient

app = Flask(__name__, instance_relative_config=False)
api = Api(app)
CORS(app)


def init_app():
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        db.create_all()

        from Application.api.jwt.jwt import authenticate, identity
        JWT(app, authenticate, identity)

    api.add_resource(Register, '/register')
    api.add_resource(Clients, '/clients')
    api.add_resource(GetNameClient, '/clients/names')
    api.add_resource(DeleteClient, '/clients/delete')

    return app
