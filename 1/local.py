#-*- coding:utf-8 -*-
import sys

from flask import Flask

from weixin import weixin_api

app = Flask(__name__)
app.debug = True
app.register_blueprint(weixin_api, url_prefix='/weixin')

if __name__ == '__main__':
    app.run()


