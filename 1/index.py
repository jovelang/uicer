#-*- coding:utf-8 -*-
import sys

from flask import Flask
from bae.core.const import APP_NAME, APP_DIR, APP_TMPDIR
from bae.core.wsgi import WSGIApplication
sys.path.insert(0, APP_DIR + '/lib')

app = Flask(__name__)
app.debug = True
application = WSGIApplication(app)

@app.route('/')
def index():
    return 'Index Page'
