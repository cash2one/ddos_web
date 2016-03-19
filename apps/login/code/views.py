# -*- coding: utf-8 -*-
from models import get_users
from tornado import gen
import tornado.web
import json
from libs import log
from libs.base_handler import BaseHandler

class LoginHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        # users = get_users()
        # self.write(json.dumps(users))
        log.debug("testt")
        self.render('../apps/login/templates/login.html')
    def post(self):
        # users = get_users()
        # self.write(json.dumps(users))
        # log.debug(self.request)
        # log.debug(self.request.body)
        # log.debug(self.get_argument("userName"))

        self.set_secure_cookie("user", self.get_argument("userName"))
        # print self.request
        # self.render('../apps/login/templates/login.html')
        self.redirect("/")


class LoginOut(BaseHandler):
    def get(self):
        self.set_secure_cookie("user", "",expires_days=1)
        self.render("/login/",error="")
    
    def post(self):
        self.set_secure_cookie("user", "",expires_days=1)
        self.render("/login/",error="Password Error")
