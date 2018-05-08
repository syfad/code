#!/usr/bin/env python
# coding:utf-8
#Auth:SunYunfeng
#sun_admin@126.com

import os

# cmd = 'tail -f /dmdata/logs/nginx/space_here_cn_access.nginx.log'
# os.system(cmd)

import time

def follow(therile):
    therile.seek(0,2)

    while True:
        line=therile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == '__main__':
    logfile = open("space_here_cn_access.nginx.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        print line