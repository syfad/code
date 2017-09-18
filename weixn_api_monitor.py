#!/usr/bin/env python
# -*- coding: utf8 -*-
#Auth:SunYunfeng
#sun_admin@126.com
#检测网站响应状态及状态花费时间

import os,sys
import time
import pycurl
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def mail_to(code):
    code = str(code)
    sender = 'sunyunfeng@6clue.com'
    receiver = 'sunyunfeng@6clue.com'
    subject = '微信API（api.weixin.qq.com）监控报警'
    smtpserver = 'smtp.mxhichina.com.'
    username = 'sunyunfeng@6clue.com'
    password = 'zaq1@wsx'


    msg = MIMEText( code, 'text', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.mxhichina.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


URL="http://58.246.220.31/sns/oauth2/access_token?appid=wx8d925967f5c4749f&secret=34e545c55273b339af1ce97fbe3b6968&code=001Otzms1TGzbp0s82ms1YWBms1OtzmG&grant_type=authorization_code"
c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)
c.setopt(pycurl.TIMEOUT, 5)
c.setopt(pycurl.NOPROGRESS, 1)
c.setopt(pycurl.FORBID_REUSE, 1)
c.setopt(pycurl.MAXREDIRS, 1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)

indexfile = file('E:\pycharm\worke\content.txt', 'wb')

c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)

try:
    c.perform()
except Exception,e:
    print "connecion error:"+str(e)
    indexfile.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = str(c.getinfo(c.HTTP_CODE))
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

# print "HTTP状态码： %s" % (HTTP_CODE)
# print "DNS解析时间：%.2f ms" % (NAMELOOKUP_TIME*1000)
# print "建立连接时间：%.2f ms" % (CONNECT_TIME*1000)
# print "准备传输时间：%.2f ms" % (PRETRANSFER_TIME*1000)
# print "传输开始时间：%.2f ms" % (STARTTRANSFER_TIME*1000)
# print "传输结束总时间：%.2f ms" % (TOTAL_TIME*1000)
# print "下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD)
# print "HTTP头部大小： %d bytes/s" %(HEADER_SIZE)
# print "平均下载速度： %d bytes/s" %(SPEED_DOWNLOAD)
indexfile.close()
c.close()

if int(HTTP_CODE) == 200:
    print 0
else:
    print 1