#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paste.script.templates import NoDefault, Template, var
from paste.util.template import paste_script_template_renderer


class Boilerplate(Template):
    _template_dir = 'templates'
    summary = 'A boilerplate for Flask project'
    required_templates = []
    vars = [
        var('app_name', 'Flask application name', default=NoDefault),
        var('description', 'One-line description of the package'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
    ]
    template_renderer = staticmethod(paste_script_template_renderer)

    def check_vars(self, vars, command):
        return Template.check_vars(self, vars, command)
