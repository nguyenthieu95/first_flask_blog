from time import time
import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_name = time()
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_filename = str(random_name) + file_ext
    picture_path = os.path.join(current_app.root_path, "static/images/profile", picture_filename)
    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)
    return picture_filename

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request",
                  sender="noreply@demo.com",
                  recipients=[user.email])
    msg.body = "To reset your password, visit the folowwing link:\n" + \
               url_for('users.reset_token', token=token, _external=True) + ".\n" + \
               "If you did not make this request then simply ignore this email and no changes will be make!"
    mail.send(msg)


