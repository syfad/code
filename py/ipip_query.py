#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 20181212
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x
#在ipip.net 查询坐标经纬度，调百度地图接口查询具体地址，写入mongodb


from pyquery import PyQuery as pq
import requests
import json
from mongo_db import MongoDBPipeline
from pymongo import MongoClient


def find_ip():
    conn = MongoClient('192.168.100.133', 20301)
    db = conn.space
    my_set = db.master_where
    ip = my_set.find({})
    for item in my_set.find().sort([("_id", -1)]).limit(1):
        # print(item['ip'])
        return item['ip']


def web_result():
    host = 'https://www.ipip.net/ip.html'
    values = {"ip": find_ip()}
    headers = {
        "Host": "www.ipip.net",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.ipip.net/ip.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    }
    res = requests.post(host, data=values, headers=headers).text

    doc = pq(res)
    data = doc('table:eq(0)')
    poi = data('tr:eq(5)').find('span').eq(0).text()
    location = data('td:eq(1)').find('span').eq(0).text()
    return poi


def baiduMap():
    baidu_ak = "49TovMFRN4X4MTk9jXU8s9a9"
    baidu_conv = "http://api.map.baidu.com/geoconv/v1/?"
    baidu_geocoder = "http://api.map.baidu.com/geocoder/v2/?"
    res = requests.get(baidu_geocoder + "output=json&location=%s&pois=1&ak=%s" % (web_result(), baidu_ak))
    rs = json.loads(res.text)['result']
    Address = rs['formatted_address']
    lat = rs['location']['lat']
    lng = rs['location']['lng']
    # print(Address)
    # print(lat)
    # print(lng)

    conn = MongoClient('192.168.100.133', 20301)
    db = conn.space
    my_set = db.master_where
    # ip = my_set.find({})

    for item in my_set.find().sort([("_id", -1)]).limit(1):
        if 'address_info' in item.keys() == True:
            exit()
        else:
            my_set.update_one({'_id': item['_id']}, {'$set': {"address_info": Address, "lat": lat, "lng": lng}})


if __name__ == '__main__':
    try:
        baiduMap()
        print('sucess')
    except:
        print('master where?')