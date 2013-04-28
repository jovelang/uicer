#coding:utf-8

from flask import Blueprint, request, current_app as app

from utils import db, APIClient as WeiboClient
from weibo.models import Token, Weibo

APP_KEY = '330457405'
APP_SECRET = 'fdf309bef2ec167668b6cde8688f0952'
CALLBACK_URL = 'http://lvyaojia.sinaapp.com/'

weibo = Blueprint('weibo', __name__)
weibo_client = WeiboClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

@weibo.route('/')
def index():
    return 'this will be worked as weibo api'

@weibo.route('/update_token', methods=['POST'])
def update_token():
    if request.method == 'POST':
        access_token = request.form.get('access_token', '')
        expires_in = request.form.get('expires_in', '')
        if access_token and expires_in:
            token = Token(access_token, int(expires_in))
            db.session.add(token)
            db.session.commit()
            return "update successfully"
    return "failed"

@weibo.route('/post_weibo')
def post_weibo():
    pass

@weibo.route('/get_token')
def get_lastest_token():
    token = Token.query.order_by('-id').first()
    return str((token.access_token, token.expires_in))
