#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint
from settings import TEMPLATE_PATH

wiki_b = Blueprint("wiki_b", __name__, template_folder=TEMPLATE_PATH)
from . import views
