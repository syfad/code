#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng
# @Disc    :
# @Disc    : support python 2.x and 3.x

# import Mysqldb
import pymysql
import sys


def QueryDBs(sql):
    HOST = '192.168.100.182'
    USER = 'dmdevelop'
    PASS = 'develop@dm.com'
    connection = pymysql.connect(host=HOST, user=USER, password=PASS, charset='utf8')
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception, e:
        print e
    finally:
        connection.close()


def status(code):
    query_code = 'SHOW GLOBAL STATUS LIKE "%s"' % code
    # query_status = dict(QueryDBs(query_code))
    query_status = QueryDBs(query_code)
    # print (query_status[code])
    print(query_status[0][1])


# print status('Questions')
# print status('Com_select')
# print status('Com_insert')
# print status('Com_update')
# print status('Com_delete')
# Writes = Com_insert + Com_update + Com_delete

# -------------查询性能------------------
# print status('Uptime')#运行时间
# print status('Slow_queries')#慢查询数量


# --------mysql连接性，可用性监控-------------
# SHOW VARIABLES LIKE 'max_connections';
# Threads_connected#当前开放的连接
# Threads_running#当前运行的连接
# Connection_errors_internal#有服务器错误导致的失败连接数
# Aborted_connects#尝试与服务器进行连接结果失败的次数
# Connection_errors_max_connections#由 max_connections 限制导致的失败连接数


if __name__ == '__main__':
    status(sys.argv[1])
