#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


# !/usr/bin/python
# -*- coding:utf-8 -*-

import urllib.request
from urllib import parse
from urllib import request
import urllib
import json

class ZabbixAPI:
    def __init__(self):
        self.__url = 'http://monitor.demai.com:8080/zabbix/api_jsonrpc.php'
        self.__user = 'admin'
        self.__password = 'zabbix@6clue.com'
        self.__header = {"Content-Type": "application/json-rpc"}
        self.__token_id = self.UserLogin()

    # 登陆获取token
    def UserLogin(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.__user,
                "password": self.__password
            },
            "id": 0,
        }
        return self.PostRequest(data)

    # 推送请求
    def PostRequest(self, data):
        request = urllib.request.Request(self.__url, json.dumps(data).encode('utf-8'), self.__header)
        result = urllib.request.urlopen(request)
        response = json.loads(result.read().decode('utf-8'))
        try:
            # print response['result']
            return response['result']
        except KeyError:
            raise KeyError

    # 主机列表
    def HostGet(self, hostid=None, hostip=None):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "selectGroups": "extend",
                "selectParentTemplates": ["templateid", "name"],
                "selectInterfaces": ["interfaceid", "ip"],
                "selectInventory": ["os"],
                "selectItems": ["itemid", "name"],
                "selectGraphs": ["graphid", "name"],
                "selectApplications": ["applicationid", "name"],
                "selectTriggers": ["triggerid", "name"],
                "selectScreens": ["screenid", "name"]
            },
            "auth": self.__token_id,
            "id": 1,
        }
        if hostid:
            data["params"] = {
                "output": "extend",
                "hostids": hostid,
                "sortfield": "name"
            }
        return self.PostRequest(data)

    # 主机列表
    def HostCreate(self, hostname, hostip, groupid=None, templateid=None):
        data = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": hostname,
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": hostip,
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": [
                    {
                        "groupid": groupid
                    }
                ],
                "templates": [
                    {
                        "templateid": templateid
                    }
                ]
            },
            "auth": self.__token_id,
            "id": 1,
        }
        return self.PostRequest(data)

    # 主机组列表
    def HostGroupGet(self, hostid=None, itemid=None):
        data = {
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "itemids": itemid,
                "sortfield": "name"
            },
            "auth": self.__token_id,
            "id": 1,
        }
        return self.PostRequest(data)

    # 监控项列表
    def ItemGet(self, hostid=None, itemid=None):
        data = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "itemids": itemid,
                "sortfield": "name"
            },
            "auth": self.__token_id,
            "id": 1,
        }
        return self.PostRequest(data)

    # 模板列表
    def TemplateGet(self, hostid=None, templateid=None):
        data = {
            "jsonrpc": "2.0",
            "method": "template.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "templateids": templateid,
                "sortfield": "name"
            },
            "auth": self.__token_id,
            "id": 1,
        }
        return self.PostRequest(data)

    # 图像列表
    def GraphGet(self, hostid=None, graphid=None):
        data = {
            "jsonrpc": "2.0",
            "method": "graph.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "graphids": graphid,
                "sortfield": "name"
            },
            "auth": self.__token_id,
            "id": 1,
        }
        return self.PostRequest(data)

    # 历史数据
    def History(self, itemid, data_type):
        data = {
            "jsonrpc": "2.0",
            "method": "history.get",
            "params": {
                "output": "extend",
                "history": data_type,
                "itemids": itemid,
                "sortfield": "clock",
                "sortorder": "DESC",
                "limit": 30
            },
            "auth": self.__token_id,
            "id": 2
        }
        return self.PostRequest(data)

    def host_scan(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host"
                ],
                "selectInterfaces" : [
                    "interfaceid",
                    "ip"
                ]
            },
            "auth": self.__token_id,
            "id": 2
        }
        return self.PostRequest(data)


def main():
    zapi = ZabbixAPI()
    token = zapi.UserLogin()
    print(token)

    hosts = zapi.host_scan()
    print(hosts)
if __name__ == '__main__':
    main()

