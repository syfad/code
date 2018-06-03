#!/usr/bin/python
#coding:utf-8

import pymysql
import ConfigParser
import sys

HOST = '192.168.100.182'
USER = 'root'
PASS = '182@root.com'

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

def get_data():
    sql = 'show slave status'
    data = QueryDBs(sql)
    return data

def get_io_status():
    data = get_data()
    io = data[0]['Slave_IO_Running']
    print io
    if io == 'Yes':
        print 1
        return 1
    else:
        return 0

def get_sql_status():
    data = get_data()
    sql = data[0]['Slave_SQL_Running']
    print sql
    if sql == 'Yes':
        print 1
        return 1
    else:
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print"Usage: %s [io|sql]" % sys.argv[0]
        sys.exit(1)
    if sys.argv[1] == "io":
        print get_io_status()
    elif sys.argv[1] == "sql":
        print get_sql_status()
