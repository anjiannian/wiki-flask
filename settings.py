#!/usr/bin/env python
# encoding: utf-8

import os

SECRET_KEY = 'aads'

MONGODB_SETTINGS = {
                    "DB": "wiki",
                    "HOST": "127.0.0.1",
                    "PORT": 27017
                    }

# Path for use
BASE_PATH = os.path.dirname(__file__)
STATIC_PATH = os.path.join(BASE_PATH, 'static')
TEMPLATE_PATH = os.path.join(BASE_PATH, 'templates')

