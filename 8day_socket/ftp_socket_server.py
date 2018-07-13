#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    :
# @Disc    : support python 2.x and 3.x

import socket
import os
import hashlib

server = socket.socket()
server.bind(("127.0.0.1", 8990))

server.listen(5)

while True:
    conn, adder = server.accept()
    print("New Conn...:", adder)

    while True:
        data = conn.recv(1024)
        print("等待新的指令...")
        if not data:
            print("客户端已断开...")
            break

        cmd, filename = data.decode().split()

        print(filename)

        if os.path.isfile(filename):
            f = open(filename, "rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(file_size)    #send file size
            conn.recv(1024)     #wait for ack
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5", m.hexdigest())
            f.close()
        print("send done")


server.close()