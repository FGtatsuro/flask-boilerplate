#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paste.script.templates import NoDefault, Template, var


class Boilerplate(Template):
    _template_dir = 'templates'
    summary = 'A boilerplate for Flask project'
    required_templates = []
    vars = [
        var('app_name', 'Flask application name', default=NoDefault),
    ]

    def check_vars(self, vars, command):
        return Template.check_vars(self, vars, command)
