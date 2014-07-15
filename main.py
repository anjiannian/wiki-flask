#!/usr/bin/env python
# encoding: utf-8

import settings
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, static_folder=settings.STATIC_PATH)
app.config.from_pyfile("settings.py")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_b.login"
login_manager.session_protection = None

db = MongoEngine(app)


def register_blueprints(app):
    from auth import auth_b
    from wiki import wiki_b
    from auth.models import User

    app.register_blueprint(auth_b)
    app.register_blueprint(wiki_b)

    @login_manager.user_loader
    def load_user(username):
        return User.objects.get(username=username)


if __name__ == '__main__':
    register_blueprints(app)
    app.debug = True
    app.run(host="0.0.0.0", port=2406, threaded=True)
