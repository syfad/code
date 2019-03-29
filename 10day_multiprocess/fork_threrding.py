#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


# -*- coding:utf-8 -*-
import os

print('当前进程:%s 启动中 ....' % os.getpid())
pid = os.fork()

if pid == 0:
    print('子进程:%s,父进程是:%s' % (os.getpid(), os.getppid()))
else:
    print('进程:%s 创建了子进程:%s' % (os.getpid(),pid ))

#fork函数会返回两次结果，因为操作系统会把当前进程的数据复制一遍，然后程序就分两个进程继续运行后面的代码，fork分别在父进程和子进程中返回，在子进程返回的值pid永远是0，在父进程返回的是子进程的进程id。


# 进程是资源（CPU、内存等）分配的基本单位，它是程序执行时的一个实例。程序运行时系统就会创建一个进程，并为它分配资源，然后把该进程放入进程就绪队列，进程调度器选中它的时候就会为它分配CPU时间，程序开始真正运行。
# Linux系统函数fork()可以在父进程中创建一个子进程，这样的话，在一个进程接到来自客户端新的请求时就可以复制出一个子进程让其来处理，父进程只需负责监控请求的到来，然后创建子进程让其去处理，这样就能做到并发处理。

