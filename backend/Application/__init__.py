from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# API
from .api.register import Register
from .api.users import Users


from .api.clients import Clients
from .api.clients.names import ClientsNames
from .api.clients.singleclient import SingleClient

from .api.bills import Bills
from .api.bills.singlebill import SingleBill

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

    # User resources
    api.add_resource(Register, "/register")
    api.add_resource(Users, "/user/me")

    # Client resources
    api.add_resource(Clients, "/clients")
    api.add_resource(SingleClient, "/clients/<int:client_id>")
    api.add_resource(ClientsNames, "/clients/names")

    # Bill resources
    api.add_resource(Bills, "/bills")
    api.add_resource(SingleBill, "/bills/<int:bill_id>")

    return app
