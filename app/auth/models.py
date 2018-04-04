import peewee as pw

from config import db
from datetime import datetime
from flask import current_app as app
from playhouse.shortcuts import model_to_dict

from .utils import generate_sid
from .mixins import WithJSONField


class User(db.Model):
    username = pw.CharField(25, index=True)
    password = pw.CharField(40, index=True)
    firstname = pw.CharField(50)
    lastname = pw.CharField(50)
    is_active = pw.BooleanField(default=True)
    is_superuser = pw.BooleanField(default=False)

    @property
    def as_dict(self):
        return model_to_dict(self, exclude=(User.password, User.is_active))

    class Meta:
        table_name = 'users'


class SessionStore(db.Model, WithJSONField):
    sid = pw.CharField(primary_key=True, index=True)
    user = pw.ForeignKeyField(User)
    expired = pw.DateTimeField()

    def save(self, user=None):
        if self.sid:
            return super().save()

        self.sid = generate_sid(user.username)
        self.expired = datetime.utcnow() + app.permanent_session_lifetime
        self.user = user

        return super().save(force_insert=True)

    class Meta:
        table_name = 'sessions'
