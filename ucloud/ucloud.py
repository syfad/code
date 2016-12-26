#!/usr/bin/env python
# -*- coding: utf-8 -*-
#auth:SunYunfeng

from sdk import UcloudApiClient
from config import *
import sys
import json
import time

#实例化 API 句柄
if __name__=='__main__':
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters={
        "Action":"RefreshUcdnDomainCache",
        "DomainId":"ucdn-nszwra",
        "Type":"file",
        "UrlList.0":"http://file.demai.com/face/2644441/face.jpg"
            }

    response = ApiClient.get("/", Parameters);

    json_str =  json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
    data = json.loads(json_str)
    taskid = data.get(u'TaskId')
#    print  taskid
#    time.sleep(30)


    args = {
        "Action": "DescribeRefreshCacheTask",
        "DomainId": "ucdn-nszwra",
        "TaskId": "%s" %(taskid)
    }

    while True:
        responsetask = ApiClient.get("/", args);
        cachetask = json.dumps(responsetask, sort_keys=True, indent=4, separators=(',', ': '))
        taskdata = json.loads(cachetask)
        data2 = (taskdata.get(u'TaskSet'))
#        print data2[0].get(u"Status")
        if  data2[0].get(u"Status") == 'success':
            print '0'
            break
        elif data2[0].get(u"Status") == 'failure':
            print '1'
            break
        else:
            time.sleep(20)
