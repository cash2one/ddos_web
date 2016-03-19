import tornado.web
from code.views import UsersHandler

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")

urls_perfix = "/demo"

urls_suffix = [
    (r'/', IndexHandler),
    (r'/users', UsersHandler),
    # (r'/', IndexHandler),
    # "/", IndexHandler,
]

# print "in-demo-url:",urls_suffix,type(urls_suffix)