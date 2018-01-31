#!/usr/bin/python
#coding:utf-8
import pymysql
import sys
class check_mysql_repl():
    def __init__(self):
        self.dbhost = 'localhost'
        self.dbuser = 'root'
        self.dbpass = 'wisp888'
        self.dbport = 3306
        self.sock = "/data/db_misc/mysql_3306.sock"
        self.conn = pymysql.connect(unix_socket=self.sock) #根据实际情况连接
        self.cursor = self.conn.cursor(cursorclass = pymysql.cursors.DictCursor)
        self.sql = 'show slave status'
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchall()
        self.io = self.data[0]['Slave_IO_Running']
        self.sql = self.data[0]['Slave_SQL_Running']
        self.conn.close()
    def get_io_status(self):
        if self.io == 'Yes':
            print 1
            return 1
        else:
            return 0
    def get_sql_status(self):
        if self.sql == 'Yes':
            print 1
            return 1
        else:
            return 0

if __name__ == "__main__":
    mysql = check_mysql_repl()
    if len(sys.argv) != 2:
        print"Usage: %s [io|sql]" % sys.argv[0]
        sys.exit(1)
    if sys.argv[1] == "io":
        print mysql.get_io_status()
    elif sys.argv[1] == "sql":
        print mysql.get_sql_status()