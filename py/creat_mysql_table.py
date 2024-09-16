#!/usr/bin/env python
#创建5天后的mysql表

import MySQLdb
import time
import datetime

#print time.strftime("%Y%m%d", time.localtime())

oneDay = (datetime.datetime.now() + datetime.timedelta(days = 5))
timeStamp = int(time.mktime(oneDay.timetuple()))
otherTime = oneDay.strftime("%Y%m%d")
#print otherTime

tablename =  'login_history_%s' %otherTime
#print tablename

#dbsql = ("CREATE TABLE %s ( `desc` varchar(11) NOT NULL DEFAULT '', `user_id` bigint(20) DEFAULT '0', `login_count` int(11) DEFAULT '0', `day` varchar(11) DEFAULT '');)") %tablename
#print dbsql


try:
        conn = MySQLdb.connect("10.9.40.180", "user", "password")
        cur = conn.cursor()
        conn.select_db('log')
        cur.execute("CREATE TABLE %s ( `desc` varchar(11) NOT NULL DEFAULT '', `user_id` bigint(20) DEFAULT '0', `login_count` int(11) DEFAULT '0', `day` varchar(11) DEFAULT '') ENGINE=MyISAM DEFAULT CHARSET=utf8 " %tablename)
        cur.close()
        conn.close()
except MySQLdb.Error, e:
        print 'Mysql Error Msg', e
