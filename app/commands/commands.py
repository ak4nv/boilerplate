import click
from app.models import User, MODELS
from app.auth.utils import get_password_hash


@click.option('--drop', default=False, type=bool,
              help='Drop table if exists. Default is False')
def initdb(drop):
    for m in MODELS:
        if m.table_exists():
            if not drop:
                click.echo('Skipped {}'.format(m.__name__))
                continue
            m.drop_table()
        m.create_table()
        click.echo('Created {}'.format(m.__name__))


def createsuperuser():
    kwargs = {'username': click.prompt('Please enter a username'),
              'firstname': click.prompt('Please enter a firstname'),
              'lastname': click.prompt('Please enter a lastname'),
              'is_superuser': True}
    password = click.prompt('Please enter a password', hide_input=True)
    confirm = click.prompt('Please confirm a password', hide_input=True)
    if password != confirm:
        raise click.BadParameter('Passwords do not match')
    User.create(password=get_password_hash(password), **kwargs)
    click.echo('User created successfully.')
