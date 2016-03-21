import tornado.web
from code.views import DomainBlackList
from code.views import DomainWhiteList
from code.views import DomainConf

urls_perfix = "/domain"

urls_suffix = [
    (r'/domain_black_list', DomainBlackList),
    (r'/domain_white_list', DomainWhiteList),
    (r'/conf', DomainConf),
]
