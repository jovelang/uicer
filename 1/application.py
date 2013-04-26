#-*- coding:utf-8 -*-
import sys

from flask import Flask
try:
    from bae.core.const import APP_NAME, APP_DIR, APP_TMPDIR, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS
    from bae.core.wsgi import WSGIApplication
except:
    local = True
    DATABASE_URI = 'mysql://root@localhost/uicer'
else:
    local = False
    DATABASE_URI = 'mysql://%s:%s@%s:%d/YhHPUHZGiGcrmrwNjSNC' % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, int(MYSQL_PORT))

from utils import db
from weixin import weixin
from weibo import weibo

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.register_blueprint(weixin, url_prefix='/weixin')
app.register_blueprint(weibo, url_prefix='/weibo')

db.init_app(app)

@app.route("/")
def index():
    return "Hello Shudong!"

if local:
    app.run()
else:
    application = WSGIApplication(app.wsgi_app)
