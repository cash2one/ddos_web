# # -*- coding: utf-8 -*-
# from models import get_users
# from tornado import gen
# import tornado.web
# import json
# from libs import log
# # from libs.base_handler import Basehandler
# from libs.base_handler import BaseHandler

# class IndexHandler(BaseHandler):
#     @gen.coroutine
#     def get(self):
#         # if not self.current_user:
#         #     self.redirect("/login/")
#         #     return
#         # users = get_users()
#         # self.write(json.dumps(users))
#         log.debug(self.current_user)
#         self.render('../apps/ace_demo/templates/index.html', name="test")
#         # self.render('../apps/index/templates/index.html')
from domain_black_list import domain_black_listHandler as DomainBlackList