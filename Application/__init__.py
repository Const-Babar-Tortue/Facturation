from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

# All blueprints have to be put under the 'db' initialization to avoid
# a circular import

# website
from .home import home_routes
from .contact import contact_routes
from .new import new_routes
from .login import login_routes
from .logout import logout_routes

# API
from .api.bills import bill_route

def init_app():
    app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")
    app.config.from_object("config.Config")

    # website
    app.register_blueprint(home_routes.home_bp)
    app.register_blueprint(contact_routes.contact_bp)
    app.register_blueprint(new_routes.new_bp)
    app.register_blueprint(login_routes.login_bp)
    app.register_blueprint(logout_routes.logout_bp)

    # API
    app.register_blueprint(bill_route.bill_api_bp)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

        return app
