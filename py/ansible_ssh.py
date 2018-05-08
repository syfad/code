#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng
# @Disc    : ssh-copy-id
# @Disc    : support python 2.x and 3.x

import os
import sys
#import pexpect


passwd = 'tttm@tttm123'
f = file("/dmdata/scripts/ip.txt", "r")

for line in f.xreadlines():
    cmd = 'ssh-copy-id -i ~/.ssh/id_rsa.pub root@%s' %(line)
    res = os.system(cmd)
    #print cmd

