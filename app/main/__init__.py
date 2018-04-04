from flask import Blueprint, render_template, redirect

bp = Blueprint('main', __name__)


@bp.route('/')
def main_page():
    # Here you can pass to `Session` object on index.html (into DOM)
    # some your application data. For ex. choices for selects
    return render_template('index.html')


@bp.route('/<path:path>')
def redir(path):
    return redirect('/')
