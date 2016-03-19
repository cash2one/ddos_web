# -*- coding: utf-8 -*-
from models import get_users
from tornado import gen
import tornado.web
import json
from libs import log
class UsersHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        users = get_users()
        # self.write(json.dumps(users))
        log.debug("testt")
        self.render('../apps/demo/templates/demo.html',users = users)