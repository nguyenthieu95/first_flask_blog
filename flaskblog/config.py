import os

class Config:
    SECRET_KEY = os.environ.get("FLASKBLOG_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("FLASKBLOG_SQLALCHEMY_DATABASE_URI")

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("FLASKBLOG_EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("FLASKBLOG_EMAIL_PASS")

