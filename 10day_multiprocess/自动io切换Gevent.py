#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import gevent

def foo():
    print('running in foo')
    gevent.sleep(2)
    print('io switch bar')

def bar():
    print('explicit contest to bar')
    gevent.sleep(1)
    print('switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])