from flask import json
from peewee import TextField, Model
from playhouse.sqlite_ext import JSONField

try:
    from playhouse.postgres_ext import BinaryJSONField
except ModuleNotFoundError:
    # Depends on psycopg2 package
    BinaryJSONField = lambda null: None


class WithBinaryJSONField(Model):
    data = BinaryJSONField(null=True)


class WithJSONField(Model):
    data = JSONField(null=True)


class WithTextField(Model):
    _data = TextField(null=True, column_name='data')
    _cached = None

    @property
    def data(self):
        if self._cached is None:
            self._cached = json.loads(self._data or '{}')
        return self._cached

    @data.setter
    def data(self, data):
        self._data = json.dumps(data)
