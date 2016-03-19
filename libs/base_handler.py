# tornado.web.RequestHandler
import tornado.web
import log

class BaseHandler(tornado.web.RequestHandler):
    # pass
    # session = 
    def get_current_user(self):
        return self.get_secure_cookie("user")
log.set_logger(level = 'DEBUG:INFO')
