:#coding:utf-8

from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/show')
def show(page):
    return 'hello world'
