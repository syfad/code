#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-19
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : support python 2.x and 3.x

import sys,os
import urllib, urllib2
import base64
import hmac
import hashlib
from hashlib import sha1
import time
import uuid
import json
from optparse import OptionParser
import ConfigParser
import traceback

access_key_id = '';
access_key_secret = '';
cdn_server_address = 'https://cdn.aliyuncs.com'
# CONFIGFILE = os.getcwd() + './access_key.ini'
# CONFIGSECTION = 'Credentials'

def percent_encode(str):
    res = urllib.quote(str.decode(sys.stdin.encoding).encode('utf8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res

def compute_signature(parameters, access_key_secret):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])

    canonicalizedQueryString = ''
    for (k,v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)

    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])

    h = hmac.new(access_key_secret + "&", stringToSign, sha1)
    signature = base64.encodestring(h.digest()).strip()
    return signature

def compose_url(user_params):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    parameters = { \
            'Format'        : 'JSON', \
            'Version'       : '2014-11-11', \
            'AccessKeyId'   : access_key_id, \
            'SignatureVersion'  : '1.0', \
            'SignatureMethod'   : 'HMAC-SHA1', \
            'SignatureNonce'    : str(uuid.uuid1()), \
            'TimeStamp'         : timestamp, \
    }

    for key in user_params.keys():
        parameters[key] = user_params[key]

    signature = compute_signature(parameters, access_key_secret)
    parameters['Signature'] = signature
    url = cdn_server_address + "/?" + urllib.urlencode(parameters)
    return url

def make_request(Path, quiet=False):
    #'ObjectType': 'Directory'
    obj = {'Action': 'RefreshObjectCaches', 'ObjectType': 'file', 'ObjectPath': 'http://yourdomain/1.txt'}
    obj['ObjectPath'] = Path
    url = compose_url(obj)
    return url

if __name__ == '__main__':
    UrlPath = make_request(sys.argv[1])
    try:
        request = urllib2.Request(UrlPath)
        response = urllib2.urlopen(request)
        content = response.read()
        print(content)
    except:
        print(sys.argv[1] + 'refresh failed!')
