#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

import threading

import time

def run(n):
    print("task", n)
    #time.sleep(2)


# t1 = threading.Thread(target=run, args=("t1"))
# t2 = threading.Thread(target=run, args=("t2"))
#
# t1.start()
# t2.start()

start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.start()
