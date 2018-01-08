#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import sys
import json
reload(sys)

#post方式传递参数

values = {
    "time": 1515428048,
    "sign": "23sfssdfsg23243434343",
    "access_token": "",
    "client": {
        "app": "JYSpace",
        "app_version": "1.0.0",
        "os_type": "iOS",
        "os_version": "10.2",
        "channel": "appstore",
        "device_id": "98D3DD6B-9AAB-46A8-8E0B-A327CF33F597",
        "device_model": "x86_64",
        "network": "Wifi/SSID"
    },
    "data": {
        "platform": 1,
        "data": {
            "mobile": "13520178800",
            "verify_code": "2342"
        }
    }
}
#values["account"]= "13822737"
#values["pwd"]="36a966bc28e34060e698f9f8a3603e9d"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
data = urllib.urlencode(values)
headers = {"User-Agent" : user_agent}
url = "http://space.here.cn/account/login"

request = urllib2.Request(url, json.dumps(values), headers)
respose = eval(urllib2.urlopen(request).read())

token = respose['data']
print respose

#print values
#print data
