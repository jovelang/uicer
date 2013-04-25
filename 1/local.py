#-*- coding:utf-8 -*-
import sys

from flask import Flask

from weixin.api import weixin_api

app = Flask(__name__)
app.debug = True
app.register_blueprint(weixin_api)

@app.route('/')
def hello():
    return "Hello, world! - Flask\n" + weixin_api

if __name__ == '__main__':
    app.run()


