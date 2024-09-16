#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import time
import threading

event = threading.Event()

def lighter():
    count = 0
    while True:
        if count > 5 and count < 10:  #改成红灯
            event.clear()   #把标志位清了
            print("\033[41;1mred light is on....\033[0m")
        elif count > 10:
            event.set()     #变绿灯
            count =0
        else:
            print("\033[42;1mgreen light is on....\033[0m")

        time.sleep(1)
        count +=1

#def car()

light = threading.Thread(target=lighter,)
light.start()