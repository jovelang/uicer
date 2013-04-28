#coding:utf-8

import requests

from utils import APIClient as WeiboClient

APP_KEY = '330457405'
APP_SECRET = 'fdf309bef2ec167668b6cde8688f0952'
CALLBACK_URL = 'http://lvyaojia.sinaapp.com/'


#授权用户的账号密码
USERID = 'lvyaojia@gmail.com'
USERPASSWD = ''


def get_access_token_from_weibo(client):
    '''模拟web用户授权，获取access_token
    '''
    params = {'action':'submit', 'withOfficalFlag':0, 'ticket':'',
        'isLoginSina':'', 'response_type':'code','state':'','from':''}
    params['redirect_uri'] = CALLBACK_URL
    params['client_id'] = APP_KEY
    params['userId'] = USERID
    params['passwd'] = USERPASSWD
    headers = {'Referer': client.get_authorize_url()}
    response = requests.post("https://api.weibo.com/oauth2/authorize", params=params, headers=headers)
    if not response.url.find('code'):
        #判断url 是否包含code, 有可能账号密码错误。
        raise Exception, 'wrong pwd'
    code = response.url.split('=')[1][0:-5]
    access_token = client.request_access_token(code)
    return access_token


