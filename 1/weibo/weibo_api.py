#coding:utf-8

from flask import Blueprint

weibo = Blueprint('weibo', __name__)

@weibo.route('/')
def index():
    return 'this will be worked as weibo api'

@weibo.route('/update_token')
def update_token():
    pass

@weibo.route('/get_token')
def get_token():
    pass

@weibo.route('/post_weibo')
def post_weibo():
    pass
