# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html', is_b2b=current_user.is_b2b)

@blueprint.route('/<template>')
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'
        return render_template( template, is_b2b=current_user.is_b2b)

    except TemplateNotFound:
        return render_template('page-404.html', is_b2b=False), 404
    
    except:
        return render_template('page-500.html', is_b2b=False), 500
