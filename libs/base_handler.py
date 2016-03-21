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
        if self.current_user:
            return tornado.escape.xhtml_escape(self.current_user)
        return ""

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

    def render_or_api_result(self,uri, method="GET", args=None):
        data = self.get_api_result(uri, method, args)
        code = data.get("code")
        if code == 0:
            return data
        self.render("ace_base/errors.html",errors="%s" % data.get("msg"))


    def render(self, template_name, where=SELF_TEMPLATES, **kwargs):
        
        if not kwargs.has_key("name"):
            # if self.user_name:
            kwargs["name"] = self.user_name

        if where == SELF_TEMPLATES:
            template_name = template_name

        super(RealBaseHandler,self).render(template_name,**kwargs)

class DebugBaseHandler(RealBaseHandler):
    api_path = "api"
    def get_api_result(self,uri, method="GET", args=None):

        uri = uri[1:].replace("/","_")
        try:
            with open("%s/%s_%s.json"%(self.api_path,uri,method), "r") as f:
                data = json.loads(f.read())

        except Exception as e:
            data = {
                "code":1,
                "msg":"sth error: %s" % e
            }
        
        return data
    
BaseHandler = DebugBaseHandler