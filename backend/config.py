from os import environ


class Config:
    # General
    TESTING = environ.get("TESTING")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")
    JWT_AUTH_HEADER_PREFIX = 'Bearer'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///./data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("TRACK_MODIFICATION")
