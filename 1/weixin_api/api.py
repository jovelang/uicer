#coding:utf-8

from flask import Blueprint

weixin_api = Blueprint('weixin_api', __name__)

@weixin_api.route('/show')
def show():
    return 'hello world'
