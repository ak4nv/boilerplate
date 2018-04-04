from flask import Blueprint, jsonify, request, session

from . import views

bp = Blueprint('auth', __name__)
options = {'url_prefix': '/auth'}

bp.add_url_rule('/login', view_func=views.login, methods=('POST',))
bp.add_url_rule('/logout', view_func=views.logout, methods=('POST',))
