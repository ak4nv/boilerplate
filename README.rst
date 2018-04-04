Simple boilerplate for web apps
===============================

This is a simple boilerplate for web apps (aka SPA — Single Page Applications) with minimum dependencies. Ideally for start a new project like an internal information system.

Dependencies
------------

- `Flask <http://flask.pocoo.org/>`_ (Web server)
- `Peewee <https://github.com/coleifer/peewee>`_ (ORM layer)
- `Marshmallow <https://github.com/marshmallow-code/marshmallow>`_ (JSON schema)
- `Marshmallow Peewee <https://github.com/klen/marshmallow-peewee>`_ (JSON schema generator from Peewee models)
- `Vue.js <https://vuejs.org>`_ (Progressive JavaScript Framework)
- `Spectre <https://picturepan2.github.io/spectre/>`_ (Lightweight, Responsive and Modern CSS Framework)

Install
-------

..  code:: shell

  git clone git@github.com:ak04nv/boilerplate.git
  cd boilerplate
  virtualenv -p python3 --prompt="(boilerplate) " .env
  . .env/bin/activate
  pip install -r requirements.txt
  export FLASK_APP=wsgi.py
  export FLASK_DEBUG=1
  flask run

Open http://localhost:5000 in your browser and use admin:admin for log in.

Commands
--------

.. code:: shell

  # Initialize database (create tables)
  # Key --drop boolean for drop table if exists (default is False)

  flask initdb --drop True

  # Create superuser
  flask createsuperuser

