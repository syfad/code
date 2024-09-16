#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import socket

client = socket.socket()

client.connect(('127.0.0.1',9999))

while True:
    cmd = input(b">>>>>>>>>:").strip()  #python2.X 需要raw_input
    if len(cmd) == 0:continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server response:", server_response)

        client.send(b"ready to recv file")
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new","wb")

        while received_size < file_total_size:
            data = client.recv(1024)
            received_size +=len(data)
            f.write(data)
            print(file_total_size,received_size)
        else:
            print("file recv done")
            f.close()

client.close(0)