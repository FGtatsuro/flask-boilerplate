#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for

from . import app
from .models import *

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/items')
def items():
    items = Dummy()
    return render_template('items.html', items=items)
