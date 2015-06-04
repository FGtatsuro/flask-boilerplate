#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)
    if app.debug:
        DebugToolbarExtension(app)

    from .views import main
    app.register_blueprint(main)
    return app
