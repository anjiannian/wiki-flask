#!/usr/bin/env python
# encoding: utf-8

from main import db
from datetime import datetime


class Wiki(db.Document):
    title = db.StringField()
    author = db.StringField()
    content = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())
