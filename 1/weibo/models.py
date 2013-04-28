#coding: utf-8

from utils import db

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String(64))
    expires_in = db.Column(db.Integer)

    def __init__(self, access_token, expires_in):
        self.access_token = access_token
        self.expires_in = expires_in

    def __repr__(self):
        return '<Token %r>' % self.access_token

class Weibo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    author = db.Column(db.String(64))
    source = db.Column(db.String(64))
    create_time = db.Column(db.DateTime, default='CURRENT_TIMESTAMP')

    def __init__(self, content, author, source):
       self.content = content
       self.author = author
       self.source = source

    def __repr__(self):
        return '<Weibo %r:%r>' % (self.author, self.content)


