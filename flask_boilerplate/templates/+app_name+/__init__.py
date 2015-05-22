#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

if app.debug:
    app.config['SECRET_KEY'] = 'debug_secretkey'
else:
    app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
DebugToolbarExtension(app)

from .controllers import *
