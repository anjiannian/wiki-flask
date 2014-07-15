#!/usr/bin/env python
# encoding: utf-8

import hashlib
from datetime import datetime
from main import db
from flask.ext.login import UserMixin


class User(UserMixin, db.Document):
    username = db.StringField(max_length=64)
    password_hash = db.StringField(max_length=128)
    email = db.EmailField(max_length=128)
    created_at = db.DateTimeField(default=datetime.now())

    def encrypt(self, plain):
        return hashlib.sha512(plain).hexdigest()

    @property
    def password(self):
        raise Exception(u"Plain text is not available")

    @password.setter
    def password(self, plain_password):
        self.password_hash = self.encrypt(plain_password)

    def verify_password(self, plain_password):
        return self.password_hash == self.encrypt(plain_password)

    def get_id(self):
        return unicode(self.username)
