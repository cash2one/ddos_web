# -*- coding: utf-8 -*-
from models import get_users
from tornado import gen
import tornado.web
import json
from libs import log
# from libs.base_handler import Basehandler
from libs.base_handler import BaseHandler

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('../apps/index/templates/index.html',name = self.user_name)