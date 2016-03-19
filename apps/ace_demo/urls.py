import tornado.web
from code.views import IndexHandler


urls_perfix = "/ace_demo"

urls_suffix = [
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/home', IndexHandler),
    # (r'/', IndexHandler),
    # "/", IndexHandler,
]

# print "in-demo-url:",urls_suffix,type(urls_suffix)