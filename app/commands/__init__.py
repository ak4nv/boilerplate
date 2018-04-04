from .commands import initdb, createsuperuser


def register_commands(app):
    app.cli.command(short_help='Manage tables in database.')(initdb)
    app.cli.command(short_help='Create superuser.')(createsuperuser)
