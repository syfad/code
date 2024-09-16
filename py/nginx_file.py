#!/usr/bin/env python
# coding:utf-8
#Auth:SunYunfeng
#sun_admin@126.com

# cddmd = 'tail -f /dmdata/logs/nginx/space_here_cn_access.nginx.log'
# os.system(cmd)

import time
import json
import os

os.chdir("/dmdata/logs/nginx/")

def follow(therile):
    therile.seek(0,2)

    while True:
        line=therile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

#countall='/chat/notice/countall'
#countall='/favicon.ico'
countall='/'


if __name__ == '__main__':
    logfile = open("space_here_cn_access.nginx.log", "r")
    countall_num = 0
    loglines = follow(logfile)
    for line in loglines:
        dist=eval(line)
        url=dist['url']
        #return url
        #xff=dist['xff']
        if url == countall:
            countall_num+=1
            print countall_num