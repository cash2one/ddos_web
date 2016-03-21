#coding:utf-8
from libs.base_handler import BaseHandler
import tornado
from libs import log


class DomainBlackList(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        view_args = {}
        view_args["page"] = int(self.get_argument("page", "1"))
        view_args["per_page"] = int(self.get_argument("per_page", "10"))
        view_args["search_sip"] = self.get_argument("search_sip","")
        view_args["search_dip"] = self.get_argument("search_dip","")
        
        args = {
                "condition":{
                        "sip":view_args["search_sip"],
                        "dip":view_args["search_sip"],
                        "page":view_args["page"],
                        "per_page":view_args["per_page"]
                }
        }

        res = self.render_or_api_result("/domain/black_list", args=args)

        view_args["count"] = res.get("data",{}).get("total", "")/view_args["per_page"] + 1
        view_args["entries"]  = res.get("data",{}).get("domain_black_list", "")
        self.render("../apps/domain/templates/domain_black_list.html",**view_args)

class DomainWhiteList(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        view_args = {}
        view_args["page"] = int(self.get_argument("page", "1"))
        view_args["per_page"] = int(self.get_argument("per_page", "10"))
        view_args["search_sip"] = self.get_argument("search_sip","")
        view_args["search_dip"] = self.get_argument("search_dip","")

        args = {
                "condition":{
                        "sip":view_args["search_sip"],
                        "dip":view_args["search_sip"],
                        "page":view_args["page"],
                        "per_page":view_args["per_page"]
                }
        }

        res = self.render_or_api_result("/domain/white_list", args=args)

        view_args["count"] = res.get("data",{}).get("total", "")/view_args["per_page"] + 1
        view_args["entries"]  = res.get("data",{}).get("domain_black_list", "")
        self.render("../apps/domain/templates/domain_white_list.html",**view_args)


class DomainConf(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        res = self.render_or_api_result("/domain/conf")
        view_args = res.get("data",{})
        self.render("../apps/domain/templates/domain_conf.html",**view_args)