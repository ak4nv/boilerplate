from flask import jsonify, request, session
from .utils import get_password_hash
from .models import User


def login():
    data = request.get_json()
    username, password = data.get('username'), data.get('password')
    if username and password:
        try:
            user = User.get(username=username,
                            password=get_password_hash(password))
        except User.DoesNotExist:
            return jsonify(errors='Wrong username or password')
        if not user.is_active:
            return jsonify(errors='Your account is disabled.\
                                   Contact to administrator')
        session.bind_to_user(user)
        return jsonify(user=user.as_dict)
    return jsonify(errors='Wrong sent data')


def logout():
    session.delete()
    return jsonify(msg='Logged out successfully')
