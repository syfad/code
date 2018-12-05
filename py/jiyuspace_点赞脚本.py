#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 20181205
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import requests
import urllib2
import time
import json

# 获取时间戳
timestr = int(time.time())


def login():
    # post方式传递参数
    values = {
        "time": timestr,
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
                "mobile": "18611938847",
                "verify_code": "9783"
            }
        }
    }
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    # data = urllib.urlencode(values)
    headers = {"User-Agent": user_agent}
    url = "http://space.here.cn/account/login"
    request = urllib2.Request(url, json.dumps(values), headers)
    respose = eval(urllib2.urlopen(request).read())
    return respose['data']['token']


def addzan(target_id):
    address = 'http://space.here.cn/thumb/thumbup'
    data = {
        "client_info": {
            "app": "jiyuspace",
            "app_version": "2.15",
            "version": "1.0",
            "type": "unknown",
            "platform_type": "other",
            "os_version": "1.0",
            "channel": "h5",
            "device_id": "9e4c89a9-b3a2-4b8b-bca9-d3867564d7f7",
            "device_model": "",
            "network": ""
        },
        "access_token": login(),
        "uid": 2619599,
        "data": {
            "type": 1,
            "target_id": target_id
        }
    }
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    # data = urllib.urlencode(values)
    headers = {"User-Agent": user_agent}
    request = urllib2.Request(address, json.dumps(data), headers)
    respose = eval(urllib2.urlopen(request).read())
    return respose


print addzan('598316356d653302e95dabf3')
