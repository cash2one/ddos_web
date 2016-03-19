import tornado.web
from code.views import DomainBlackList


urls_perfix = "/domain"

urls_suffix = [
    # (r'/', IndexHandler),
    (r'/domain_black_list', DomainBlackList),
    # (r'/home', IndexHandler),
    # (r'/', IndexHandler),
    # "/", IndexHandler,
]

# print "in-demo-url:",urls_suffix,type(urls_suffix)