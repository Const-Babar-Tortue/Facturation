from wtforms import StringField, SubmitField, Form, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired(), Email(message="Enter a valid email")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
