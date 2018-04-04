from flask import abort, redirect, request, session
from functools import wraps


def role_required(*roles):
    def decor(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if set(roles) & set(session.user.roles):
                return f(*args, **kwargs)
            return abort(403)
        return wrapper
    return decor


def superuser_required(*roles):
    def decor(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if session.user.superuser:
                return f(*args, **kwargs)
            return abort(403)
        return wrapper
    return decor
