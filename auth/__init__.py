#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint
from settings import TEMPLATE_PATH

auth_b = Blueprint("auth_b", __name__, template_folder=TEMPLATE_PATH)
from . import views
