from libs.base_handler import BaseHandler
import hashlib
import tornado
from libs import log

class LoginHandler(BaseHandler):
    def get(self):
        self.render("../apps/login/templates/login.html",error="")

    @tornado.gen.coroutine
    def post(self):
        name = self.get_argument("loginname")
        passwd = self.get_argument("logpasswd")

        if not name or not passwd:
            self.render("../apps/login/templates/login.html",error="user or passwd is null!")
            return

        uri = "/login"
        method = "POST"
        args = {
            "name":name,
            "passwd":passwd,
        }

        res = self.get_api_result(uri, method, args)
        if res.get("code") != 0:
            self.render("../apps/login/templates/login.html",error="%s" % res.get("msg"))
            return

        self.set_secure_cookie("user", self.get_argument("loginname"),expires_days=1)
        
        # log.info(self.get_argument("next", "/"))
        self.redirect(self.get_argument("next", "/"))
        
class LoginOut(BaseHandler):
    def get(self):
        self.set_secure_cookie("user", "",expires_days=1)
        self.redirect("/login")
    
    def post(self):
        self.set_secure_cookie("user", "",expires_days=1)
        self.redirect("/login")