#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 201
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

import socket

client = socket.socket()

client.connect(('192.168.100.132',6866))

while True:
    cmd = raw_input(b">>>>>>>>>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd)

    cmd_res_size = client.recv(1024) #接受命令结果的长度
    print("commant size:",cmd_res_size) #命令结果大小
    #client.send("准备好接受了")

    received_size = 0
    #received_data = b''

    while received_size != int(cmd_res_size):
        cmd_res = client.recv(1024)
        received_size +=len(cmd_res) #每次收到有可能小于1024，所以必须用len判断
        #print received_size
        print(cmd_res)
    else:
        print ('received done!', received_size)


client.close()