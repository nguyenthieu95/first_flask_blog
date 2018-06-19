from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


### Extension object created outside of function make importable to another package
db = SQLAlchemy()                            # database instances
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'        # function name of route
login_manager.login_message_category = 'info'   # message color for bootstrap when logged in.
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    ### Init extension object inside creation application
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    ### Blueprint
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app


