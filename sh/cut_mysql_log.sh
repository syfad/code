#!/usr/bin/env bash
#auth sunyunfeng

LogName=mysql-error.log
LogPath=/dmdata/logs/mysql

mv $LogPath/$LogName $LogPath/`date +%Y%m%d`$LogName
/dmdata/server/mysql/bin/mysqladmin -uroot -p'root@182.com' --socket=/dmdata/tmp/mysql.sock flush-logs
find $LogPath -ctime +7 -exec rm -f {} \;