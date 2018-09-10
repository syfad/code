#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

import urllib2

#from urllib import request
from gevent import monkey
import gevent, time

monkey.patch_all()  #把当前程序所有的IO操作，单独做上标记

def f(url):
    print('GET: %s' % url)
    response = urllib2.Request(url)
    resp = urllib2.urlopen(response)

    #resp = request.urlopen(url)
    data = resp.read()
    f = open("url.html", "wb")
    f.write(data)
    f.close()
    print('%d bytes received from %s' %(len(data), url))

urls = [
    'https://www.yahoo.com/',
    'https://github.com/',
    'http://sina.com/'
]

time_start = time.time()

for url in urls:
    f(url)
print("同步cost：", time.time() - time_start)


async_time = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
    gevent.spawn(f, 'http://sina.com/')
])

print("异步cost：", time.time() - async_time)