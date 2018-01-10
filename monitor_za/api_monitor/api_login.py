#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import sys
import json
import time
import pymysql
reload(sys)

# HOST = '172.16.0.148'
# USER = 'readonly'
# PASS = '8I&MI0czhKDF%agS'
#
# def QueryDB(sql):
#     connection = pymysql.connect(host=HOST, user=USER, password=PASS, charset='utf8')
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute(sql)
#             result = cursor.fetchone()
#             return result[0]
#     except Exception, e:
#         print e
#     finally:
#         connection.close()
#
# def get_access_token():
#     sql = 'SELECT token FROM space.sessions where platform=11 AND uid=2619599'
#     access_token=QueryDB(sql)
#     return access_token

#获取时间戳
timestr=int(time.time())

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
                "mobile": "15678150743",
                "verify_code":"9783"
            }
        }
    }
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    #data = urllib.urlencode(values)
    headers = {"User-Agent" : user_agent}
    url = "http://space.6clue.com/account/login"
    request = urllib2.Request(url, json.dumps(values), headers)
    respose = eval(urllib2.urlopen(request).read())
    return respose

def login_status():
    data = login()
    return data['errno']

def uid():
     data = login()
     uid = data['data']['uid']
     return uid

def token():
    data = login()
    token = data['data']['token']
    return token

