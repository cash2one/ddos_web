import tornado.web
from code.views import CurrentDetail
from code.views import DayDetail
from code.views import WeekDetail
from code.views import MonthDetail
from code.views import YearDetail


urls_perfix = "/all_traffic"

urls_suffix = [
    (r'/', CurrentDetail),
    (r'/current', CurrentDetail),
    (r'/day_detail', DayDetail),
    (r'/week_detail', WeekDetail),
    (r'/month_detail', MonthDetail),
    (r'/year_detail', YearDetail),

]
