from datetime import timedelta

# How to generate SECRET_KEY
# python3 -c 'import os; print(os.urandom(24))'
SECRET_KEY = b'\n\xc6\x9a\xe9\xbf\x08Y\x99\x1b\xf6l\x8a\xdfZ\x9f9\xef\x01&\x0e\x1a&\xc1Q'
APP_NAME = 'Web App Boilerplate'
PERMANENT_SESSION_LIFETIME = timedelta(hours=8)
ADMINS = ('admin@example.com',)

SESSION_COOKIE_NAME = 'sid'

JSON_AS_ASCII = False

DATABASE_URL = 'sqliteext:///db_test.sqlite'

# URL prefix for ajax requests
# https://github.com/axios/axios#request-config
BASE_URL = ''
# Default settings for send emails of exceptions
# For fast sending use celery or local smtp-proxy
# https://github.com/ak04nv/smtp-proxy
MAIL_SERVER = 'localhost'
MAIL_PORT = 1025
MAIL_DEFAULT_SENDER = '{} <{}>'.format(APP_NAME, ADMINS[0])
MAIL_USERNAME = 'mail_account'
MAIL_PASSWORD = 'strong_password'
MAIL_USE_TLS = False
