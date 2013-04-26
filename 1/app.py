#-*- coding:utf-8 -*-
import sys

from flask import Flask
try:
    from bae.core.const import APP_NAME, APP_DIR, APP_TMPDIR
    from bae.core.wsgi import WSGIApplication
    sys.path.insert(0, APP_DIR + '/lib')
except:
    local = True
else:
    local = False

from weixin import weixin
from weibo import weibo

app = Flask(__name__)
app.debug = True
app.register_blueprint(weixin, url_prefix='/weixin')
app.register_blueprint(weibo, url_prefix='/weibo')

@app.route("/")
def index():
    return "Hello Shudong!testing branch"

if local:
    app.run()
else:
    application = WSGIApplication(app.wsgi_app)
