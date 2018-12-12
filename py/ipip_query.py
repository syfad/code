#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


from pyquery import PyQuery as pq
import requests
import json
from mongo_db import MongoDBPipeline


def find_ip():
    DB = {'address': '192.168.100.186:20301,192.168.100.133:20301', 'db': 'space', 'col': 'master_where',
          'replicaSet': 'dmmongo'}
    find_obj = MongoDBPipeline(DB['db'], DB['col'], DB['address'], DB['replicaSet'])
    ipadd = find_obj.find({})['ip']
    ip = ipadd.encode("utf-8")
    # print(ip)
    return ip


def web_result():
    host = 'https://www.ipip.net/ip.html'
    values = {"ip": find_ip()}
    headers = {
        "Host": "www.ipip.net",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.ipip.net/ip.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    }
    res = requests.post(host, data=json.dumps(values), headers=headers).text
    return res


def getaddres():
    doc = pq(web_result())
    data = doc('table').eq(1)
    location = data('td')('span').eq(0).text()
    return location


def save_addres():
    DB = {'address': '192.168.100.186:20301,192.168.100.133:20301', 'db': 'space', 'col': 'master_where',
          'replicaSet': 'dmmongo'}
    find_obj = MongoDBPipeline(DB['db'], DB['col'], DB['address'], DB['replicaSet'])
    ipadd = find_obj.find({})
    newaddres = {}
    print(ipadd)

save_addres()
