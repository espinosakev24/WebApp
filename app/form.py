from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField("Full name", validators=[DataRequired(),Length(min=5, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")
