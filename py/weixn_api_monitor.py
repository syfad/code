#!/usr/bin/env python
# coding:utf-8
#Auth:SunYunfeng
#sun_admin@126.com
#检测网站响应状态及状态花费时间可结合zabbix报警

import os,sys
import time
import pycurl
from io import BytesIO

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


# #URL="http://58.246.220.31/sns/oauth2/access_token?appid=wx8d925967f5c4749f&secret=34e545c55273b339af1ce97fbe3b6968&code=001Otzms1TGzbp0s82ms1YWBms1OtzmG&grant_type=authorization_code"
# URL="https://api.mch.weixin.qq.com/pay/unifiedorder"
# #URL="https://api.mch.weixin.qq.com/pay/unifiedorder"
# c = pycurl.Curl()
# #c = pycurl.CURL_HTTP_VERSION_1_1
#
# c.setopt(pycurl.SSL_VERIFYHOST, 2)
# c.setopt(pycurl.URL, URL)
# c.setopt(pycurl.CONNECTTIMEOUT, 5)
# c.setopt(pycurl.TIMEOUT, 5)
# c.setopt(pycurl.NOPROGRESS, 1)
# c.setopt(pycurl.FORBID_REUSE, 1)
# c.setopt(pycurl.MAXREDIRS, 1)
# c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
#
# #c.setopt(pycurl.CURLOPT_SSLVERSION, 3)
#
# indexfile = open('/Users/sun_admin/Documents/sunyf/pycharm/content.txt', 'wb')
#
# c.setopt(pycurl.WRITEHEADER, indexfile)
# c.setopt(pycurl.WRITEDATA, indexfile)
#
# try:
#     c.perform()
# except Exception as e:
#     print("connecion error:"+str(e))
#     indexfile.close()
#     sys.exit()
#
# NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
# CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
# PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
# STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
# TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
# HTTP_CODE = str(c.getinfo(c.HTTP_CODE))
# SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
# HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
# SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)
#
# print (u"HTTP状态码： %s" % (HTTP_CODE))
# print (u"DNS解析时间：%.2f ms" % (NAMELOOKUP_TIME*1000))
# print (u"建立连接时间：%.2f ms" % (CONNECT_TIME*1000))
# print (u"准备传输时间：%.2f ms" % (PRETRANSFER_TIME*1000))
# print (u"传输开始时间：%.2f ms" % (STARTTRANSFER_TIME*1000))
# print (u"传输结束总时间：%.2f ms" % (TOTAL_TIME*1000))
# print (u"下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD))
# print (u"HTTP头部大小： %d bytes/s" %(HEADER_SIZE))
# print (u"平均下载速度： %d bytes/s" %(SPEED_DOWNLOAD))
#
# print("########################################")
# print("返回的HTTP状态码:", c.getinfo(pycurl.HTTP_CODE))         #返回的HTTP状态码
# print("传输结束所消耗的总时间", c.getinfo(pycurl.TOTAL_TIME))        #传输结束所消耗的总时间
# print("DNS解析所消耗的时间", c.getinfo(pycurl.NAMELOOKUP_TIME))   #DNS解析所消耗的时间
# print("建立连接所消耗的时间", c.getinfo(pycurl.CONNECT_TIME))      #建立连接所消耗的时间
# print("从建立连接到准备传输所消耗的时间", c.getinfo(pycurl.PRETRANSFER_TIME))  #从建立连接到准备传输所消耗的时间
# print("从建立连接到传输开始消耗的时间", c.getinfo(pycurl.STARTTRANSFER_TIME))    #从建立连接到传输开始消耗的时间
# print("重定向所消耗的时间", c.getinfo(pycurl.REDIRECT_TIME))     #重定向所消耗的时间
# print("上传数据包大小", c.getinfo(pycurl.SIZE_UPLOAD))       #上传数据包大小
# print("下载数据包大小", c.getinfo(pycurl.SIZE_DOWNLOAD))     #下载数据包大小
# print("平均下载速度", c.getinfo(pycurl.SPEED_DOWNLOAD))    #平均下载速度
# print("平均上传速度", c.getinfo(pycurl.SPEED_UPLOAD))      #平均上传速度
# print("HTTP头部大小", c.getinfo(pycurl.HEADER_SIZE))       #HTTP头部大小
#
#
# indexfile.close()
# c.close()


class ex_response(object):
    def __init__(self,url):
        self.buffer = BytesIO()
        self.c = pycurl.Curl()
        self.c.setopt(pycurl.URL,url)
        self.c.setopt(pycurl.WRITEDATA, self.buffer)
        self.c.setopt(pycurl.WRITEHEADER,self.buffer)
        try:
            self.c.perform()
        except Exception as e:
            print('connection error:' + str(e))
            self.buffer.close()
            self.c.close()

    def getinfo(self):
        h1 = self.c.getinfo(pycurl.HTTP_CODE)  # 状态码
        h2 = self.c.getinfo(pycurl.TOTAL_TIME)  # 传输结束总消耗时间
        h3 = self.c.getinfo(pycurl.NAMELOOKUP_TIME)  # DNS解析时间
        h4 = self.c.getinfo(pycurl.CONNECT_TIME)  # 建立连接时间
        h5 = self.c.getinfo(pycurl.PRETRANSFER_TIME)  # 建立连接到准备传输消耗时间
        h6 = self.c.getinfo(pycurl.STARTTRANSFER_TIME)  # 从建立连接到传输开始消耗时间
        h7 = self.c.getinfo(pycurl.REDIRECT_TIME)  # 重定向消耗时间
        h8 = self.c.getinfo(pycurl.SIZE_UPLOAD)  # 上传数据包大小
        h9 = self.c.getinfo(pycurl.SIZE_DOWNLOAD)  # 下载数据包大小
        h10 = self.c.getinfo(pycurl.SPEED_DOWNLOAD)  # 平均下载速度
        h11 = self.c.getinfo(pycurl.SPEED_UPLOAD)  # 平均上传速度
        h12 = self.c.getinfo(pycurl.HEADER_SIZE)  # http头文件大小
        info ='''
            http状态码：%s
            传输结束总时间：%.2f ms
            DNS解析时间：%.2f ms
            建立连接时间：%.2f ms
            准备传输时间：%.2f ms
            传输开始时间：%.2f ms
            重定向时间：%.2f ms
            上传数据包大小：%d bytes/s
            下载数据包大小：%d bytes/s
            平均下载速度：%d bytes/s
            平均上传速度：%d bytes/s
            http头文件大小：%d byte
        ''' %(h1,h2*1000,h3*1000,h4*1000,h5*1000,h6*1000,h7*1000,h8,h9,h10,h11,h12)
        print(info)
        self.buffer.close()
        self.c.close()

if __name__ == '__main__':
    curl_respon = ex_response("https://api.mch.weixin.qq.com/pay/unifiedorder")
    curl_respon.getinfo()




# if int(HTTP_CODE) == 200:
#     print 0
# else:
#     print 1
