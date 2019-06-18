#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


#import Mysqldb
import pymysql

HOST = '192.168.100.182'
USER = 'dmdevelop'
PASS = 'develop@dm.com'


# HOST = '172.16.0.99'
# USER = 'demai'
# PASS = 'XCHSYwy6293_NZ7210nv_NS*QDm'

def insertDB(sql):
    connection = pymysql.connect(host=HOST, user=USER, password=PASS, charset='utf8')
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
    except Exception, e:
        print e
    finally:
        connection.close()


def QueryDB(sql):
    connection = pymysql.connect(host=HOST, user=USER, password=PASS, charset='utf8')
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
    except Exception, e:
        print e
    finally:
        connection.close()


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

def QueryDBs_dict(sql):
    connection = pymysql.connect(host=HOST, user=USER, password=PASS, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception, e:
        print e
    finally:
        connection.close()


def UpdatDB(sql):
    connection = pymysql.connect(host=HOST, user=USER, password=PASS, charset='utf8')
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
    except Exception, e:
        with open(logPath, "a") as obj:
            obj.writelines(__name__ + "    UpdatDB     " + str(e) + "    %s    " % ctime() + os.linesep)
    finally:
        connection.close()
