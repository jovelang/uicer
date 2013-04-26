#coding:utf-8

from flask import Blueprint

weibo = Blueprint('weibo', __name__)

@weibo.route('/')
def index():
    return 'this will be worked as weibo api'
