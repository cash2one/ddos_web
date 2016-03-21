#coding:utf-8
from libs.base_handler import BaseHandler
import tornado
from libs import log
import time

class CurrentDetail(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        view_args = {}
        
        view_args["day"] = int(self.get_argument("day", "20160101"))

        
        args = {
                "condition":{
                    "day":"20160101"
                }
        }

        res = self.render_or_api_result("/all_traffic/day_detail", args=args)
        view_args["entries"]  = res.get("data",{}).get("day_detail", "")
        self.render("../apps/all_traffic/templates/dashboard.html",**view_args)

class DayDetail(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        view_args = {}
        
        view_args["day"] = int(self.get_argument("day", "20160101"))

        
        args = {
                "condition":{
                    "day":"20160101"
                }
        }

        res = self.render_or_api_result("/all_traffic/day_detail", args=args)
        view_args["entries"]  = res.get("data",{}).get("day_detail", "")
        self.render("../apps/all_traffic/templates/day_detail.html",**view_args)

class WeekDetail(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        view_args = {}
        
        view_args["day"] = int(self.get_argument("day", "20160101"))

        
        args = {
                "condition":{
                    "day":"20160101"
                }
        }

        res = self.render_or_api_result("/all_traffic/week_detail", args=args)
        view_args["entries"]  = res.get("data",{}).get("week_detail", "")
        self.render("../apps/all_traffic/templates/week_detail.html",**view_args)

class MonthDetail(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        view_args = {}
        
        view_args["day"] = int(self.get_argument("day", "20160101"))

        args = {
                "condition":{
                    "day":"20160101"
                }
        }

        res = self.render_or_api_result("/all_traffic/month_detail", args=args)
        view_args["entries"]  = res.get("data",{}).get("month_detail", "")
        self.render("../apps/all_traffic/templates/month_detail.html",**view_args)

class YearDetail(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        view_args = {}
        
        view_args["day"] = int(self.get_argument("day", "20160101"))

        
        args = {
                "condition":{
                    "day":"20160101"
                }
        }

        res = self.render_or_api_result("/all_traffic/year_detail", args=args)
        view_args["entries"]  = res.get("data",{}).get("year_detail", "")
        self.render("../apps/all_traffic/templates/year_detail.html",**view_args)