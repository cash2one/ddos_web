#!/usr/bin/env python
#coding:utf-8
from base import BaseHandler
import tornado
from ddos_dev.ddos_dev_api import DdosDevApi as API
from limits_conf import *

class domain_confHandler(BaseHandler):
    def get(self):
        user = self.get_secure_cookie("user")
        if not user: self.render("login.html",error = "")
        name = tornado.escape.xhtml_escape(self.current_user)
        qx = quanxian(self,name,"get",18)
        if qx.get_limits():
            return
        page = self.get_argument("page", 1)
        search_sip = self.get_argument("search_sip")
        search_dip = self.get_argument("search_dip")

        entries = self.db.query("select id,block_prompt,prompt_enable,match_mode from match_http_contrl")
        
        if entries == []:
            entries = [{}]
            entries[0]["id"] = ""
            entries[0]["block_prompt"] = ""
            entries[0]["prompt_enable"] = ""
            entries[0]["match_mode"] = ""

        print entries
        print "===============================123"
        self.render("domain_conf.html",entries = entries,name=name,page=page,search_sip=search_sip,search_dip=search_dip)
        
        
    def post(self):
        
        user = self.get_secure_cookie("user")
        if not user: self.render("login.html",error = "")
        namelogin = tornado.escape.xhtml_escape(self.current_user)
        qx = quanxian(self,namelogin,"get",18)
        if qx.get_limits():
            return
        ids = self.get_argument("id")
        block_prompt = self.get_argument("block_prompt")
        try:
            prompt_enable = self.get_argument("prompt_enable")
        except:
            prompt_enable = 'off'
        match_mode = self.get_argument("match_mode")
         
        
        
        page = self.get_argument("page")
        search_sip = self.get_argument("search_sip")
        search_dip = self.get_argument("search_dip")
        
        if ids == "":
            query = "INSERT INTO match_http_contrl (block_prompt,prompt_enable,match_mode) VALUES ('%s','%s','%s')"%(block_prompt,prompt_enable,match_mode)
        else:
            query = "update match_http_contrl set block_prompt='%s',prompt_enable='%s',match_mode='%s' where id=%s"%(block_prompt,prompt_enable,match_mode,ids)
     
        print "router_addHandler post"
        print query
        try:
            self.db.execute(query)
        except:
            self.redirect("domain_conf?page=%s&search_sip=%s&search_dip=%s"%(page,search_sip,search_dip))
            return
        ddos_list = self.db.query("select ip,port from system_config_table")
        if prompt_enable == "on":
            http_prompt_enable = True
        else:
            http_prompt_enable = False

        for ddos in ddos_list:
            a = API(host=ddos["ip"], port=ddos["port"])
            msg = a.match_http_rule_c(match_http_mode = match_mode, http_prompt=block_prompt,http_prompt_enable=http_prompt_enable)
    #def match_http_rule_c(self, match_http_mode=None,http_prompt=None, http_prompt_enable=None):
            #print type(rules)
            #print rules
            print msg
            if msg["code"] == 0:
                pass
        self.redirect("domain_conf?page=%s&search_sip=%s&search_dip=%s"%(page,search_sip,search_dip))
