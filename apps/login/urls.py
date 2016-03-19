import tornado.web
from code.views import LoginHandler

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")

urls_perfix = "/login"

urls_suffix = [
    # (r'/', LoginHandler),
    (r'', LoginHandler),
    # (r'/', IndexHandler),
    # "/", IndexHandler,
]

# print "in-demo-url:",urls_suffix,type(urls_suffix)