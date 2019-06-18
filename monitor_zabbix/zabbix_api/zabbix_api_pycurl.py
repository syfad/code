#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import os,sys
import time
import pycurl
import smtplib
from urllib.parse import urlencode
from io import StringIO

c = pycurl.Curl()
c.setopt(c.URL,'http://monitor.demai.com:8080/zabbix/api_jsonrpc.php')
c.setopt(c.HTTPHEADER, ["Content-Type: application/json-rpc"])

post_data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
    "user": "Admin",
    "password": "zabbix@6clue.com"
        },
    "id": 0,
}

postfields = urlencode(post_data)
c.setopt(pycurl.POSTFIELDS,postfields)
c.perform()


if c.getinfo(pycurl.RESPONSE_CODE) ==200:
    html = StringIO.getvalue()

c.close()
print(html)