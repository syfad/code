#!/bin/bash
# Name: mysql_backup.sh
# Author: SunYunfeng
# Usage: ./mysql_backup.sh

# 定义mysqldump命令文件全路径
#MYSQLDUMP='/home/local/mysql/bin/mysqldump'
MYSQLDUMP='/usr/local/mysql/bin/mysqldump'

# 定义开始时间
Begin=`date "+%Y年%m月%d日 %H时%M分%S秒"`

# 定义前1天的时间
DTIME=`date -d "1 day ago" +%Y%m%d%H`

# 定义7天前的时间
D7AGO=`date -d "7 day ago" +%Y%m%d%H`

# 定义日志目录
LogFile=/dmdata/logs/mysqldump_full_backup.log

# 定义备份目录
#MYSQLBAKDIR='/storage/data/mysqlbak'
MYSQLBAKDIR='/dmdata/backups/mysqlbak'

# 密码
MYSQLPASS='you passwod'

# mysqldump备份参数

PAR1='--max_allowed_packet=4194304'

PAR2='--net_buffer_length=16384'

PAR3='--default-character-set=utf8'

# 定义要备份哪些库
#MYSQLDATALIST='admin area circle dming feed file memcached relation report stat user'
Mysql_dbname=(admin area circle dming feed file memcached relation report stat user pay)

# 创建备份目录(日期命名)

mkdir -p $MYSQLBAKDIR/$DTIME

# 备份指定库

for dname in "${Mysql_dbname[@]}"
    do
        $MYSQLDUMP -u root --password="$MYSQLPASS" $PAR1 $PAR2 $PAR3 $dname>$MYSQLBAKDIR/$DTIME/${dname}_${DTIME}.sql
    done

End=`date "+%Y年%m月%d日 %H时%M分%S秒"`

echo -e  "开始备份时间:$Begin -e 结束时间:$End  "

# 切换到备份目录
cd ${MYSQLBAKDIR}

# 开始打包

Begin_tar=`date "+%Y年%m月%d日 %H时%M分%S秒"`

tar zcf ${DTIME}_148.tar.gz ${DTIME}

End_tar=`date "+%Y年%m月%d日 %H时%M分%S秒"`

# 日志输出：记录备份时长跟打包时长
echo -e  "开始备份时间:${Begin}  备份结束时间:${End} 数据库:${Mysql_dbname[@]} backup  successfully  " >>$LogFile

echo -e  "开始打包时间:${Begin_tar}  打包结束时间:${End_tar}  tar successfully \n" >>$LogFile

# 删除 10 天前的备份文件
find $MYSQLBAKDIR  -maxdepth 1 -mtime +10 -exec rm -rf  {} \;


