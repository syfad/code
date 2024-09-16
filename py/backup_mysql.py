#!/usr/bin/env python
# -*- coding: utf-8 -*-
#auth:sunyunfeng(sunyfad@gmail.com)
#定时任务，进入备份目录执行脚本

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
import os
import datetime

today = str(datetime.date.today())
back_dir = '/dmdata/backups/mysqlbackup/'

def mail_to(code):
    code = str(code)
    sender = 'sunyunfeng@6clue.com'
    receiver = 'sunyunfeng@6clue.com'
    subject = '打听mysql数据备份'
    smtpserver = 'smtp.mxhichina.com.'
    username = 'sunyunfeng@6clue.com'
    password = 'tttm@tttm123'


    msg = MIMEText( code, 'text', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.mxhichina.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def backupdata():
    #back_dir = '/dmdata/backups/mysqlbackup/'
    #back_dir = '/Users/sun_admin/'
    print "####检查安装目录......"
    if os.path.exists(back_dir):
        print(back_dir+ "已存在目录,开始备份!")
    else:
        os.system('mkdir' +back_dir)
    os.system('cd ' +back_dir)
    print("####安装目录正常......")

    print "开始执行备份语句!"
    cmd = '/dmdata/server/mysql/bin/mysqldump  -h 172.16.0.159 -uroot -pfYrqSUr3qptg -S /dmdata/data/mysql/db/mysql.sock -e  --default-character-set=utf8 --max_allowed_packet=4194304 --net_buffer_length=16384 --databases talk-online >' +back_dir+ 'talk-online.sql'
    res = os.system(cmd)
    if res != 0:
        code = "语句执行失败"
        mail_to(code)
    else:
        code = '语句执行完成，备份成功'

    print "压缩数据"
    os.system('cd ' + back_dir)
    cmd = 'tar -czf talk-online' + today + '.tar.gz talk-online.sql'
    os.system(cmd)
    os.system('rm -f talk-online.sql')
    mail_to(code)


if __name__ == '__main__':
    backupdata()
