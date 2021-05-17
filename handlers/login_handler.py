# coding: utf-8

import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    """登陆接口"""
    def post(self):
        user_name = self.get_argument('name')
        passwd = self.get_argument('passwd')



