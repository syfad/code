#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x
# server:socket_server

import socket

cli = socket.socket()
cli.connect(('localhost', 9999))

while True:
    cmd = raw_input(">>>>>>:").strip()
    if len(cmd) == 0:continue
    cli.send(cmd)
    data = cli.recv(1024)
    print("recv:",data)

cli.close()