#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

import Queue


q = Queue.Queue()           #先入 先出
q1= Queue.LifoQueue()       #后进 先出
q2= Queue.PriorityQueue()   #存储数据时可设置优先级的队列


# for i in range(100):
#     q.put(i)
#     print(q.get())

for i in range(100):
    q.put(i)
    print(q.get())


# q1.put(1)
# q1.put(2)
# q1.put(3)
# print(q1.get())
# print(q1.get())
# print(q1.get())
#
# q2.put((1, "syf"))
# q2.put((3, "sssf"))
# q2.put((100, "sdfsd"))
# print(q2.get())
# print(q2.get())
# print(q2.get())
