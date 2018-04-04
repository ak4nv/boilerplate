from flask import request_started
from playhouse.flask_utils import FlaskDB
from playhouse.signals import Model as SignalModel


class DBWrapper(FlaskDB):
    # https://github.com/pallets/flask/issues/2679
    # https://github.com/coleifer/peewee/issues/1557

    def connect_db(self):
        if self.database.is_closed():
            self.database.connect()

    def close_db(self, exc):
        if not self.database.is_closed():
            self.database.close()


class SignalsDBWrapper(DBWrapper):

    def get_model_class(self):
        if self.database is None:
            raise RuntimeError('Database must be initialized.')

        class BaseModel(SignalModel):

            class Meta:
                database = self.database

        return BaseModel
