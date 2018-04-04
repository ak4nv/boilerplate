import hashlib
from flask import current_app as app
from time import time


def get_password_hash(password):
    hash = hashlib.sha1()
    hash.update(bytes(password, 'utf-8'))
    hash.update(app.config['SECRET_KEY'])
    return hash.hexdigest()


def generate_sid(username):
    hash = hashlib.sha1()
    hash.update(bytes(username, 'utf-8'))
    hash.update(app.config['SECRET_KEY'])
    hash.update(bytes(str(time()), 'utf-8'))
    return hash.hexdigest()
