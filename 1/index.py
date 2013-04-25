#-*- coding:utf-8 -*-
import sys
sys.path.insert(0, APP_DIR + '/lib')

from flask import Flask

from bae.core.const import APP_NAME, APP_DIR, APP_TMPDIR
from bae.core.wsgi import WSGIApplication

app = Flask(__name__)
app.debug = True
application = WSGIApplication(app)


@app.route('/')
def index():
    return 'Index Page'
