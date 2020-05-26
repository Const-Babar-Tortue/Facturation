from Application.models.UserTable import User


def authenticate(username, password):
    user = User.query.filter(User.username == username).first()
    if user and user.check_password(password):
        return user


def identity(payload):
    return User.query.filter(User.id == payload["identity"]).first()
