#!/usr/bin/env python
# coding:utf8

# 读取mysql配置文件
import ConfigParser
import MySQLdb
import urllib
import urllib2
import json
import subprocess
import os
import sys

class Mysql_ini:
    
    def __init__(self, path):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(path)
        
    def config(self):
        return self.cf

class Mysql:
    def __init__(self, host, user, passwd, port, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db

        try:
            self.conn = MySQLdb.connect(host=host, user=user, passwd=passwd, port=port, db=db)
	    self.cur = self.conn.cursor()
        except MySQLdb.Error, e:
            print e.args[0], e.args[1]
            sys.exit(1)

    def getOne(self, query):
        self.cur.execute(query)
        result = self.cur.fetchone()
        return int(result[1])  

    def getAll(self, query):
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def executeQuery(self, query):
        self.cur.execute(query)
        self.conn.commit()
        print "%s execute success" % (query)

    def closeConn(self):
        self.cur.close()
        self.conn.close()

def main():
    print "ok"
    ini = Mysql_ini("mysql.ini")
    cf = ini.config()
    host = cf.get('mysql', 'host')
    user = cf.get('mysql', 'user')
    passwd = cf.get('mysql', 'passwd')
    port = cf.getint('mysql', 'port')
    db = cf.get('mysql', 'db')
    mysql = Mysql(host, user, passwd, port, db)
    query_mp3_sql = 'select answer_id, question_id, origin_file, answer_file, is_converted from answer where is_converted != 1 and answer_id != 317'
    datas = mysql.getAll(query_mp3_sql)
    if len(datas) >= 1:
        for data in datas:
            mp3_url_converted(data)

def mp3_url_converted(data):
    mq = {}
    mq['answer_id'] = int(data[0])
    question_id = data[1]
    mq['origin_file'] = data[2]
    mq['answer_file'] = data[3]
    is_converted = data[4]
    question_url = 'http://dt.6clue.com/answer/wait/%d' % (question_id)
    weixin_url = 'http://weixin.6clue.com/getSignPackage.php?url=%s' % (question_url)
    weixin_json = json.loads(urllib2.urlopen(weixin_url).read())
    mq['access_token'] = weixin_json['token']

    voice_mq(mq, is_converted)


def remove_file(origin_file, answer_file):
    print origin_file, answer_file
    origin_file = '/dmdata/data/talk/origin_file/%s' % (origin_file)
    answer_file = '/dmdata/data/talk/answer_file/%s/%s/%s' % (answer_file[0:2], answer_file[2:4], answer_file)
	
    if os.path.isfile(origin_file):
	os.remove(origin_file)
    
    if os.path.isfile(answer_file):
    	os.remove(answer_file)

def voice_mq(mq, is_converted):
    print mq
    if is_converted == 3:
	    remove_file(mq['origin_file'], mq['answer_file'])
	    url = 'http://10.9.48.107:10000/audio/convert'
	    data = urllib.urlencode(mq)
	    req = urllib2.Request(url, data)
	    res_data = urllib2.urlopen(req)
	    res = res_data.read()
	    print res 
    else:
	    url = 'http://10.9.48.107:10000/audio/convert'
	    data = urllib.urlencode(mq)
	    req = urllib2.Request(url, data)
	    res_data = urllib2.urlopen(req)
	    res = res_data.read()
	    print res 
    
if __name__ == '__main__':
    main()
