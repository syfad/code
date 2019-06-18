#!/usr/bin/python
# -*- coding:utf-8 -*-
# auth：sunyunfeng（sunyfad@gmail.com）
# 我的卡券

import urllib
import urllib2
import sys
import json
import api_login

uid = api_login.uid()
token = api_login.token()

values = {
	"client_info": {
		"app": "jiyuspace",
		"app_version": "1.30",
		"version": "1.0",
		"type": "unknown",
		"platform_type": "other",
		"os_version": "1.0",
		"channel": "h5",
		"device_id": "",
		"device_model": "",
		"network": ""
	},
	"access_token": token,
	"uid": uid,
	"data": {}
}

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
# data = urllib.urlencode(values)
headers = {"User-Agent": user_agent}
url = "http://space.here.cn/center/mycoffee"
request = urllib2.Request(url, json.dumps(values), headers)
# respose = urllib2.urlopen(request).read()
respose = eval(urllib2.urlopen(request).read())


if respose['error_code'] == 0:
    print 0
    print respose
else:
    print 1
    print respose['error_msg']