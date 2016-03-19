
import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
# from url import url

from tornado.options import define, options
from libs import log
# from base import BaseHandler
log.set_logger(level = 'DEBUG:INFO')

define("port", default=88, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="ddos_system", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="Leeknet@123", help="database password")

from libs.torna_auto import auto_get_urls

log.debug(auto_get_urls(["apps/*/urls.py"]))
class Application(tornado.web.Application):
    def __init__(self):
        handlers = auto_get_urls(["apps/*/urls.py"])
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            cookie_secret = "6dsfd1oETzKXQs45432334322GaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url = "/login",
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

       
if __name__ == "__main__":
    main()
