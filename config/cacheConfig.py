from flask_caching import Cache
from .flaskConfig import flask
cache = Cache(flask,config={'CACHE_TYPE': 'simple'})