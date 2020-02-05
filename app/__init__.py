import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"#os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
db.create_all()
bcrypt = Bcrypt(app)

from app import routes
