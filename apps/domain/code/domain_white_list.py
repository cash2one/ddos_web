#!/usr/bin/env python
#coding:utf-8
from base import BaseHandler
from ddos_dev.ddos_dev_api import DdosDevApi as API
import tornado
from limits_conf import *

class domain_white_listHandler(BaseHandler):
    def get(self):
        user = self.get_secure_cookie("user")
        if not user: self.render("login.html",error = "")
        name = tornado.escape.xhtml_escape(self.current_user)
        p = int(self.get_argument("page"))
        qx = quanxian(self,name,"get",17)
        if qx.get_limits():
            return

        search_sip = self.get_argument("search_sip")
        search_dip = self.get_argument("search_dip")
        sql = ""
        if len(search_sip) != 0:
            sql = sql + "and domain = '" + search_sip + "'"
        if len(search_dip) != 0:
            sql = sql + "and dip_s = '" + search_dip + "'"
            
        #print sql
      
        if p == 0:
            p = 1  
        total = "select count(*) from domain_white where 1 = 1 " + sql
        count =  self.db.query(total)
        sums = (count[0]['count(*)'] + 50 - 1) / 50
        sql = "SELECT id,domain,whoadd,time FROM domain_white where 1 = 1 " + sql + " order by id"+ " limit 50 offset " + str((p-1) * 50)
        print sql
        entries = self.db.query(sql)
        
        #print entries
       
        self.render("domain_white_list.html",name = name, entries=entries,page = p,count=sums,search_sip=search_sip,search_dip=search_dip)
           
class domain_white_listsearchHandler(BaseHandler):
    def get(self):
        user = self.get_secure_cookie("user")
        if not user: self.render("login.html",error = "")
        name = tornado.escape.xhtml_escape(self.current_user)
        qx = quanxian(self,name,"get",17)
        if qx.get_limits():
            return
        search_sip = self.get_argument("search_sip")
        search_dip = self.get_argument("search_dip")
        p = int(self.get_argument("page"))
        
        if len(search_sip) == 0 and len(search_dip) == 0:
            self.redirect("/domain_white_list?page=%d&type=0&search_sip=&search_dip="%p)
            return
        sql = ""
        if len(search_sip) != 0:
            sql = sql + "and domain = '" + search_sip + "'"
        if len(search_dip) != 0:
            sql = sql + "and dip_s = '" + search_dip + "'"
              
        print sql
        
        if p == 0:
            p = 1  
        query = "SELECT id,domain,whoadd,time FROM domain_white where 1 = 1 " + sql + " order by id"+ " limit 50 offset " + str((p-1) * 50)
        print query
        entries = self.db.query(query)
        #print entries
        total = "select count(*) from domain_white where 1 = 1 " + sql
        #print total
        count =  self.db.query(total)
        sums = (count[0]['count(*)'] + 50 - 1) / 50
        self.render("domain_white_list.html",name = name, entries=entries,page = p,count=sums,search_sip=search_sip,search_dip=search_dip)


class domain_white_list_delHandler(BaseHandler):
    def get(self):
        user = self.get_secure_cookie("user")
        if not user: self.render("login.html",error = "")
        name = tornado.escape.xhtml_escape(self.current_user)
        qx = quanxian(self,name,"post",17)
        if qx.get_limits():
            return
        
        ids = self.get_argument("id")
        page = self.get_argument("page")
        search_sip = self.get_argument("search_sip")
        search_dip = self.get_argument("search_dip")
        
        entries= self.db.query("select domain from domain_white where id = %s", int(ids))
        if not entries:
            self.redirect("domain_white_list?page=%s&search_sip=%s&search_dip=%s"%(page,search_sip,search_dip))
            return

        domain = entries[0]["domain"]
        ddos_list = self.db.query("select ip,port from system_config_table")
        for ddos in ddos_list:
            a = API(host=ddos["ip"], port=ddos["port"])
            msg = a.domain_white_d(domain)
            if msg["code"] == 0:
                pass
        self.db.execute("delete from domain_white where id = %s", int(ids))
        
        print "=====white_domain?page=%s&search_sip=%s&search_dip=%s"%(page,search_sip,search_dip)
        
        self.redirect("domain_white_list?page=%s&search_sip=%s&search_dip=%s"%(page,search_sip,search_dip))

class domain_white_list_addHandler(BaseHandler):
    def get(self):
        user = self.get_secure_cookie("user")
        if not user: self.render("login.html",error = "")
        ids = self.get_argument("id", 0)
        name = tornado.escape.xhtml_escape(self.current_user)
        qx = quanxian(self,name,"get",17)
        if qx.get_limits():
            return
        page = self.get_argument("page", 1)
        search_sip = self.get_argument("search_sip")
        search_dip = self.get_argument("search_dip")

        entries = self.db.query("select id,domain,whoadd,time from domain_white where id = %s",int(ids))
        
        if ids == 0:
            entries = [{}]
            entries[0]["id"] = ""
            entries[0]["domain"] = ""

        print entries
        print "===============================123"
        self.render("domain_white_list_add.html",entries = entries,name=name,page=page,search_sip=search_sip,search_dip=search_dip)
        
        
    def post(self):
        
        user = self.get_secure_cookie("user")
        if not user: self.render("login.html",error = "")
        namelogin = tornado.escape.xhtml_escape(self.current_user)
        qx = quanxian(self,namelogin,"post",17)
        if qx.get_limits():
            return
        ids = self.get_argument("id")
        domain = self.get_argument("domain")

        page = self.get_argument("page")
        search_sip = self.get_argument("search_sip")
        search_dip = self.get_argument("search_dip")
        
        if ids == "":
            query = "INSERT INTO domain_white (domain,whoadd) VALUES ('%s','%s')"%(domain,namelogin)
        else:
            query = "update domain_white set domain='%s',whoadd='%s' where id=%s"%(domain,namelogin,ids)
     
        #print "router_addHandler post"
        self.log("添加域名白名单：[%s]"%domain);
        #print query
        try:
            self.db.execute(query)
        except:
            self.redirect("domain_white_list?page=%s&search_sip=%s&search_dip=%s"%(page,search_sip,search_dip))
            return
        ddos_list = self.db.query("select ip,port from system_config_table")
        for ddos in ddos_list:
            a = API(host=ddos["ip"], port=ddos["port"])
            msg = a.domain_white_c(domain)
            if msg["code"] == 0:
                pass
            else:                
                self.log("同步集群域名白名单失败：[%s]"%domain);
        self.redirect("domain_white_list?page=%s&search_sip=%s&search_dip=%s"%(page,search_sip,search_dip))
