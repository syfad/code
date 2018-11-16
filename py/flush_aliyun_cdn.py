#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import urllib
import urllib2
import time


# action= RefreshObjectCaches
# ObjectType=Directory
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent}
obj='ObjectPath=http://file.6clue.com/album/2619599/1e81261ee510ccdfbeba11408114a234.jpg'



#https://cdn.aliyuncs.com?&Action=RefreshObjectCaches&ObjectPath=test.test.com/test.txt&ObjectType=File&公共请求参数



# def flush_alicdn():
#

server_address = 'https://cdn.aliyuncs.com?&Action=RefreshObjectCaches&%s' %(obj)


# request = urllib2.Request(server_address, headers=headers)
# response = urllib2.urlopen(request)
# content = response.read()

print server_address
timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
print timestamp






# import sys,os
# import urllib, urllib2
# import base64
# import hmac
# import hashlib
# from hashlib import sha1
# import time
# import uuid
#
# class pushAliCdn:
#     def __init__(self):
#         self.cdn_server_address = 'http://cdn.aliyuncs.com'
#         self.access_key_id = 'xxxxxxxxx'
#         self.access_key_secret = 'xxxxxxxxxxxxxxxx'
#
#     def percent_encode(self, str):
#         res = urllib.quote(str.decode(sys.stdin.encoding).encode('utf8'), '')
#         res = res.replace('+', '%20')
#         res = res.replace('*', '%2A')
#         res = res.replace('%7E', '~')
#         return res
#
#     def compute_signature(self, parameters, access_key_secret):
#         sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
#         canonicalizedQueryString = ''
#         for (k,v) in sortedParameters:
#             canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)
#         stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:])
#         h = hmac.new(access_key_secret + "&", stringToSign, sha1)
#         signature = base64.encodestring(h.digest()).strip()
#         return signature
#
#     def compose_url(self, user_params):
#         timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
#         parameters = { \
#                 'Format'        : 'JSON', \
#                 'Version'       : '2014-11-11', \
#                 'AccessKeyId'   : self.access_key_id, \
#                 'SignatureVersion'  : '1.0', \
#                 'SignatureMethod'   : 'HMAC-SHA1', \
#                 'SignatureNonce'    : str(uuid.uuid1()), \
#                 'TimeStamp'         : timestamp, \
#         }
#         for key in user_params.keys():
#             parameters[key] = user_params[key]
#         signature = self.compute_signature(parameters, self.access_key_secret)
#         parameters['Signature'] = signature
#         url = self.cdn_server_address + "/?" + urllib.urlencode(parameters)
#         return url
#
#     def make_request(self, user_params, quiet=False):
#         url = self.compose_url(user_params)
#         #print url
#         #刷新url
#         try:
#             req = urllib2.Request(url)
#             res_data = urllib2.urlopen(req)
#             res = res_data.read()
#             return res
#         except:
#             return user_params['ObjectPath'] + ' refresh failed!'
#
# if __name__ == '__main__':
#     f = pushAliCdn()
#     params = {'Action': 'RefreshObjectCaches', 'ObjectPath': 'http://xxxxxxxxxx/', 'ObjectType': 'Directory'}
#     res = f.make_request(params)
#     print res

