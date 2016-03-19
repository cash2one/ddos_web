# -*- coding: utf-8 -*-
import tornado.web
import log
import json
import os 

SELF_TEMPLATES = 1
GLOBAL_TEMPLATES = 0

log.set_logger(level = 'DEBUG:INFO')

class RealBaseHandler(tornado.web.RequestHandler):
    @property
    def user_name(self):
        return tornado.escape.xhtml_escape(self.current_user)

    def get_current_user(self):
        return self.get_secure_cookie("user")

    
    @tornado.gen.coroutine
    def get_api_result(self,uri, method="GET", args=None):
        '''
        异步请求后端接口
        '''
        if args:
                req = json.dumps(args)
        else:
            req = {}
        try:
            response = yield AsyncHTTPClient().fetch(url, method=POST, body=req)
        except:
            response = None
        data = {
            "code":1,
            "msg":"sth error!"
        }
        raise tornado.gen.Return(data)
    # def get_template_path(self):
    #     pass
    def render(self, template_name, where=SELF_TEMPLATES, **kwargs):
        
        if not kwargs.has_key("name"):
            kwargs["name"] = self.user_name

        if where == SELF_TEMPLATES:
            template_name = template_name
            # template_path = self.__module__.replace('')
        # print locals()
        # print [(name, getattr(self, name)) for name in dir(self)]
        # print vars(self)
        # print self.__module__
        super(RealBaseHandler,self).render(template_name,**kwargs)

class DebugBaseHandler(RealBaseHandler):
    api_path = "api"
    def get_api_result(self,uri, method="GET", args=None):

        uri = uri[1:].replace("/","_")
        try:
            with open("%s/%s_%s.json"%(self.api_path,uri,method), "r") as f:
                data = json.loads(f.read())

        except:
            data = {
                "code":1,
                "msg":"sth error!"
            }
        return data

BaseHandler = DebugBaseHandler