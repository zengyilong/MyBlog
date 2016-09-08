# -*- coding:utf-8 -*-
"""
This script runs the MyBlog application using a development server.
"""


from os import environ
from flask_bootstrap import Bootstrap
from MyBlog import create_app

app = create_app('no')

if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug=True)
