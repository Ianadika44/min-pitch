from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)


app.config['SECRET_KEY'] = 'f7266d21c86028741a1b8f2c9ce6d43f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from pitch import routes
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
