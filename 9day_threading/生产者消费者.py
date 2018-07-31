#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import Queue
import threading

q = Queue.Queue(0)

def Producer(name):

    for i in range(10):
        q.put("apple %s" %i)




def Consumer(name):
    while q.qsize() > 0:
        print("%s eat %s..." %(name, q.get()))



p = threading.Thread(target=Producer, args=("syf",))
c = threading.Thread(target=Consumer, args=("zhangsan",))
p.start()
c.start()