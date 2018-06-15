from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd9a5b64528d72d7420e1315ddf03617'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)    # database instances
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'              # function name of route
login_manager.login_message_category = 'info'   # message color for bootstrap when logged in.

from flaskblog import routes