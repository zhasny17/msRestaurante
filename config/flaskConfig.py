# -*- coding: utf-8 -*-
from flask import Flask,jsonify

flask = Flask(__name__)
flask.config['JSON_AS_ASCII'] = False

####### CONTEXT PATH #########
class PrefixMiddleware(object):
    def __init__(self, flask, prefix=''):
        self.flask = flask
        self.prefix = prefix
    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.flask(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ['Root Path Nao encontrado, verifique se o caminho foi informado corretamente ou se existe!'.encode()]

flask.wsgi_app = PrefixMiddleware(flask.wsgi_app, prefix='/point')
