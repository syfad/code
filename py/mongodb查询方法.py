#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

from mongo_db import MongoDBPipeline
from pymongo import MongoClient
import pymysql
import time,datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')




def QueryDB(sql):
    connection = pymysql.connect(host=HOST, user=USER, password=PASS, charset='utf8')

    #cur.execute("set names 'UTF8'")
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
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


def find_tkey():
    conn = MongoClient('172.16.0.119', 20301)
    db = conn.space
    my_set = db.join_activity
    #data = my_set.find({"sku_no":"5beed1c58778787a2d048e46"})

    for item in my_set.find({"sku_no":"5beed1c58778787a2d048e46"}):
        #return item['uid']
        print(item['uid'])


uids = [
3881,
2757461,
2757323,
788608,
2767276,
2768115,
2768119,
2729767,
2756203,
2768140,
2764109,
2768156,
712801,
2768222,
2764704,
2768314,
41494,
2767879,
2766254,
2765651,
2768105,
2768621,
2768623,
2768626,
2768627,
2768628,
2704893,
2768106,
2768645,
2768649,
2768660,
2768682,
2768685,
2767525,
2768694,
2768696,
2768716,
34510,
2768722,
2768726,
2768727,
2768733,
2768736,
2768740,
2768815,
2768817,
2768821,
2768823,
2768845,
2677496,
2768854,
3879,
2768866,
2768892]


uidx = [2747956,
2770514,
2770520,
2770533,
2770513,
2770553,
2770557,
2770559,
2770562,
2770561,
2770565,
2770566,
2770567,
2770568,
2765614,
2770600,
2770605,
2770602,
2770608,
2739187,
2770615,
2770615,
2770625,
2770632,
2770637,
2770641,
2770640,
2770651,
2770656,
2770659,
2770661,
2770662,
2770668,
2770671,
2770674,
2770679,
2770680,
2770681,
2770764,
2770785,
2770788,
2770791,
2770791,
2770796,
2770797,
2770798,
2760993,
2616459,
2770818,
2770855,
2769029,
2770865,
2770865,
2770865,
2768682,
2763467,
2770870,
2754813,
2751651,
2770884,
2769475,
2770893,
2745330,
2770896,
2770897,
2768727,
2770903,
2770902,
2770904,
2768722,
2767021,
2768733,
2770919,
2770918,
2770921,
2770922,
2770923,
2770924,
2770925,
2770916,
2770631,
2770931,
2770933,
2770935,
2770938,
2770942,
2770943,
2768696,
2621432,
2770948,
2770949,
2770952,
2770953,
2768685,
2770956,
2770958,
2770979,
2769738,
2770990,
2770999,
2771001,
2771003,
2771000,
2771007,
2771016,
2771017,
2771027,
2725355,
2771047,
2771048,
2766039,
2771082,
2771088,
2771093,
2771094,
2771096,
2770170,
2771103,
2634513,
2431389,
2761150,
2771137,
2771138,
2771140,
2771139,
2771141,
2771143,
2771144,
2771142,
2771145,
2771157,
2770975,
2771198,
2771200,
2771201,
2765075,
2767525,
2766598,
2766165,
2770155,
2769565,
2766976,
2765723,
2766199,
2758702,
2769998,
2768107,
2765035,
2768106,
2771209,
2769134,
2767276,
2765953,
2768163,
2764514,
2768324,
2765658,
2771211,
2771227,
2771233,
2771234,
2771230,
2771235,
2771236,
2771250,
2771269,
2771271,
2771273,
2771275,
2771277,
2763608,
2771288,
2729767,
2771295,
2771299,
2771298,
2771300,
2771302,
2771303,
2771307,
2771310,
2771348,
2771352,
2771354,
2771363,
2771364,
2771285,
2771379,
2771377,
2771375,
2770962,
2771397,
2771408,
2771216,
48040,
34510,
29346,
3881,
3879]


def Get_One(uid):
    # sql = 'select b.tkey, b.`name`, r.company , r.post FROM `user`.basic AS b , `user`.realdata AS r  WHERE b.tkey=%s  and r.tkey=b.tkey' % (uid)
    # one_user = querysql.QueryDBs(sql)
    # return one_user
    sql = 'SELECT user.basic.tkey, user.basic.name, user.basic.time  FROM user.basic WHERE tkey=%s' %(uid)
    result = QueryDBs_dict(sql)
    date = result[0]

    tkey=date['tkey']
    name=date['name']
    time = date['time']

    stylename = name.encode('GBK')
    name1 = name.decode("unicode_escape")
    #a = eval("u" + "\'" + name + "\'")

    dateArray = datetime.datetime.utcfromtimestamp(time)
    StyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")


# for i in range(len(uidx)):
#     #uid = (uidx[i])
#     print(Get_One(uidx[i]))


HOST = '172.16.0.148'
USER = 'readonly'
PASS = '8I&MI0czhKDF%agS'

conn = pymysql.connect(host=HOST, user=USER, password=PASS, use_unicode=True, charset="utf8")
cursor = conn.cursor()
sql = 'SELECT user.basic.tkey, user.basic.name, user.basic.time  FROM user.basic WHERE tkey=2619599'
cursor.execute(sql)

res = cursor.fetchone()
a = res[1].encode('utf8')
cursor.close()
print(a)