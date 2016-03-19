# -*- coding: utf-8 -*-
from models import get_users
from tornado import gen
import tornado.web
import json
from libs import log
# from libs.base_handler import Basehandler
from libs.base_handler import BaseHandler

class IndexHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        # if not self.current_user:
        #     self.redirect("/login/")
        #     return
        # users = get_users()
        # self.write(json.dumps(users))
        log.debug(self.current_user)
        self.render('../apps/index/templates/index.html')