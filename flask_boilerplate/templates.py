#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paste.script.templates import Template


class Boilerplate(Template):
    _template_dir = 'templates'
    summary = 'A boilerplate for Flask project'
    required_templates = []
    vars = [
    ]
