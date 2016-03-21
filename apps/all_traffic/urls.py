import tornado.web
from code.views import DayDetail


urls_perfix = "/all_traffic"

urls_suffix = [
    (r'/day_detail', DayDetail),
]
