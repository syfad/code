#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    :
# @Disc    : support python 2.x and 3.x


import socket
import os
import json

client = socket.socket()

client.connect(('127.0.0.1',9999))


class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
        print(msg)

    def connect(self, ip, port):
        self.client.connect(ip, port)

    def interactive(self):
        while True:
            cmd = input(">>>>>>>:").strip()
            if len(cmd) ==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s" % cmd_str):
                func = getattr(self,"cmd_%s" % cmd_str)
                func(cmd)
            else:
                self.help()


    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action": "put",
                    "filename": filename,
                    "size": filesize
                }
                #msg_str = "%s|%s" %(filename,filesize)
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                #防止粘包，等服务器确认
                server_response = self.client.recv(1024)
                f = open(filename,"rb")
                for line in f:
                    self.client.send(line)
                else:
                    print('file upload sucess....')

            else:
                print(filename,"is not exist")



ftp = FtpClient()
ftp.connect("locahost", 9998)
ftp.interactive()