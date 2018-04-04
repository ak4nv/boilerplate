from flask.sessions import SessionMixin, SessionInterface
from werkzeug.datastructures import CallbackDict
from datetime import datetime

from .models import SessionStore


class Session(CallbackDict, SessionMixin):

    def __init__(self, store=None):
        def on_update(self):
            self.modified = True

        self._store = store
        if hasattr(store, 'data'):
            CallbackDict.__init__(self, store.data, on_update)
            self.modified = False

    @classmethod
    def find(cls, sid):
        try:
            store = SessionStore.get(sid=sid)
        except SessionStore.DoesNotExist:
            return None
        return cls(store)

    @property
    def is_expired(self):
        return self._store.expired < datetime.utcnow()

    @property
    def user(self):
        return getattr(self._store, 'user', None)

    @property
    def sid(self):
        return getattr(self._store, 'sid', None)

    def bind_to_user(self, user):
        store = SessionStore()
        store.save(user=user)
        self._store = store

    def delete(self):
        self.modified = True
        if self._store:
            self._store.delete_instance()

    def save(self):
        if hasattr(self._store, 'data') and self.modified:
            self._store.data = self
        self._store.save()


class MySessionInterface(SessionInterface):

    should_change_cookie = False

    def open_session(self, app, request):
        if request.endpoint == 'static':
            return None

        sid = request.cookies.get(app.session_cookie_name)
        if sid:
            session = Session.find(sid)
            if session is not None:
                if session.is_expired:
                    session.delete()
                else:
                    return session

        self.should_change_cookie = True
        return Session()

    def save_session(self, app, session, response):
        if self.should_change_cookie:
            domain = self.get_cookie_domain(app)
            path = self.get_cookie_path(app)

            if session.user:
                httponly = self.get_cookie_httponly(app)
                secure = self.get_cookie_secure(app)
                expires = session._store.expired
                response.set_cookie(app.session_cookie_name, session.sid,
                                    expires=expires, httponly=httponly,
                                    domain=domain, path=path, secure=secure)
            else:
                response.delete_cookie(app.session_cookie_name,
                                       domain=domain, path=path)

        if session.modified and session.user:
            session.save()
