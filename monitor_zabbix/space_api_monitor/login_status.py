#!/usr/bin/python
# -*- coding:utf-8 -*-
# auth：sunyunfeng（sunyfad@gmail.com）
# login_status


import api_login

uid = api_login.uid()
token = api_login.token()
status = api_login.login_status()

if status == 0:
    print 0
else:
    print 1