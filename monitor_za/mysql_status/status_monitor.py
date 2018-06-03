#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng
# @Disc    :
# @Disc    : support python 2.x and 3.x

# import Mysqldb
import pymysql
import sys

HOST = '192.168.100.182'
USER = 'dmdevelop'
PASS = 'develop@dm.com'

def QueryDBs(sql):
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
    query_code='SHOW GLOBAL STATUS LIKE "%s"' % code
    query_status = dict(QueryDBs(query_code))
    return (query_status[code])



print status('Questions')
print status('Com_select')
print status('Com_insert')
print status('Com_update')
print status('Com_delete')


# def Questions():
#     ques_sql='SHOW GLOBAL STATUS LIKE "Questions"'
#     question=dict(QueryDBs(ques_sql))
#     return (question['Questions'])
#
#
# def Com_Select():
#     select_sql = 'SHOW GLOBAL STATUS LIKE "Com_select"'
