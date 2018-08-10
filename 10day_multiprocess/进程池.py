#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


from multiprocessing import Process, Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)


pool = Pool(5)

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)
    # pool.apply(func=Foo, args=(i,))

print('end')
pool.close()
pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。