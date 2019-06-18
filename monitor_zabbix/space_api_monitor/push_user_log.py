#!/usr/bin/python
# -*- coding:utf-8 -*-
# auth：sunyunfeng（sunyfad@gmail.com）
#push_user_log ELK


import urllib2
import sys
import json
import api_login
import time


uid = api_login.uid()
token = api_login.token()
timestr = int(time.time())

values = {
	"atom": {
		"l_version": "1.30",
		"l_channel": "system_monitor",
		"l_os": "other",
		"l_platform": "other",
		"l_uid": uid,
		"l_uid_type": 0,
		"l_device_id": "46a5cc3f-fcd9-40ec-9060-9fefc8159dc0",
		"l_user_info_time": timestr
	},
	"data": [{
		"anchor": "main-home-recommend",
		"id": "0",
		"l_event": "page_load"
	}]
}

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
# data = urllib.urlencode(values)
headers = {"User-Agent": user_agent}
url = "https://userlog.6clue.com/push_user_log"
request = urllib2.Request(url, json.dumps(values), headers)
# respose = urllib2.urlopen(request).read()
respose = eval(urllib2.urlopen(request).read())


if respose['err_code'] == 0:
    print 0
else:
    print 1
    print respose['error_msg']
