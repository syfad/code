#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

import multiprocessing
import time
import os

def run(name):
    time.sleep(1)
    print('hello', name)

if __name__ == '__main__':
    for i in range(2):
        p = multiprocessing.Process(target=run, args=('syf %s' %i,))
        p.start()



#=================================================
#os.getppid 获得父进程PID

# def run():
#     print('program pid:', os.getppid())
#     print('process pid:', os.getpid())
#
# run()
#=================================================
