# -*- coding:utf-8 -*-

from flask import Flask, request
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def hello():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, World!</h1>\n<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    manager.run()
