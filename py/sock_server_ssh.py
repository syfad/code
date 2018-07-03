#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import socket
import os

server = socket.socket()            #绑定地址族
server.bind(('localhost', 6866))    #绑定端口
server.listen(5)                    #监听几个连接，（几个客户端意思）

while True:
    conn, addr = server.accept()
    print(addr)

    while True:
        data = conn.recv(1024)

        if not data:
            print("clien has colser...")
            break
        print("input comment:", data)

        cmd_res = os.popen(data).read()

        conn.send(str(len(cmd_res)))

        # client_ack = conn.recv(1024)
        # print(client_ack)
        conn.send(cmd_res)

server.close()
