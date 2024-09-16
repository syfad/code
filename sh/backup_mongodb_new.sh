#!/bin/sh
#auth:sunyunfeng
#mail:sun_admin@126.com

DATE=`date +%Y%m%d%H%M`
DEL_DATE=$(date -d '-3 days' "+%Y%m%d")
DEL_DATE_TAR=$(date -d '-3 days' "+%Y%m%d")
HOST="dmmongo/172.16.0.119:20301,172.16.0.130:20301"
#BACKUP_PATH="/data/backup/$DATE"
BACKUP_PATH="/storage/backups/$DATE"
MongobinPath='/home/local/mongodb/bin'

mkdir -p $BACKUP_PATH

date +%Y%m%d%H%M >>/dmdata/logs/mongodb_bak.log
start()
{
${MongobinPath}/mongodump -h $HOST --oplog  -o $BACKUP_PATH
}
execute()
{
  start
  if [ $? -eq 0 ]
  then
    echo "mongodb back successfully!" >>/dmdata/logs/mongodb_bak.log
    echo -e "Mongodb备份成功!!" | mail -s "119 $DATE MongoDB备份成功!!" ops@6clue.com
  else
    echo "mongodb back fail!" >>/dmdata/logs/mongodb_bak.log
    echo -e "Mongodb备份失败!!" | mail -s "119 $DATE MongoDB备份失败!!" ops@6clue.com
  fi
}
execute

cd /storage/backups/

tar -czf ${DATE}.tar.gz ${DATE}
scp -P 36000 ${DATE}.tar.gz root@172.16.0.118:/storage/mongodata_back

rm -rf "/storage/backups/${DEL_DATE}0130"
rm -rf "/storage/backups/${DEL_DATE_TAR}0130.tar.gz"
