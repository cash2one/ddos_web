from code.views import LoginHandler
from code.views import LoginOut


urls_perfix = "/login"

urls_suffix = [
    (r'', LoginHandler),
    (r'/logout', LoginOut),
]
