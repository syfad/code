#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import threading
import time


# def run(n):
#     print("task", n)
#     time.sleep(2)
#     print("task done", n)

lock = threading.Lock()
def run(n):
    lock.acquire()
    global num
    num +=1
    time.sleep(1)
    lock.release()

num=1

# t1 = threading.Thread(target=run, args=("t1"))
# t2 = threading.Thread(target=run, args=("t2"))
#
# t1.start()
# t2.start()

start_time = time.time()
t_object = []

for i in range(2550):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.start()
    t_object.append(t)  #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里。


for i in t_object:      #循环线程实例列表，等待所有线程执行完毕。
    t.join()

print("----all threads has finished...", threading.active_count())
#print(time.time())
#print("cost:", time.time() - start_time)
print('num:', num)