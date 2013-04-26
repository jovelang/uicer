#coding:utf-8

from flask import Blueprint

weixin = Blueprint('weixin', __name__)

@weixin.route('/')
def index():
    return 'this will be worked as weixin api'
