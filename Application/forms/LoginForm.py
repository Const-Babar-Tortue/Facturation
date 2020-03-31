from wtforms import StringField, Form, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = StringField("email", validators=[DataRequired(), Email(message="Enter a valid email")])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Log In")
