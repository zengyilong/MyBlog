# -*- coding:utf-8 -*-
from datetime import datetime
from flask import render_template
from datetime import datetime

from . import main

@main.route('/')
@main.route('/index')
def index():   
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        current_time=datetime.utcnow()
    )

@main.route('/home')
def home():
    return render_template(
        'home.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@main.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
