#!/bin/bash
#crontab 时钟同步

ntpServer=(
[0]=asia.pool.ntp.org
[1]=210.72.145.44
[2]=133.100.11.8
[3]=ntp.sjtu.edu.cn
[4]=time.scau.edu.cn
)
serverNum=`echo ${#ntpServer[*]}`
NUM=0
for (( i=0; i<=$serverNum; i++ )); do
   
    echo -n "正在和NTP服务器${ntpServer[$NUM]}校验中..."
    /usr/sbin/ntpdate ${ntpServer[$NUM]} >> /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo -e "\e[1;32m\t\t\t\t\t[成功]\e[0m"
        break
    else
        echo -e "\e[1;31m\t\t\t\t\t[失败]\e[0m"
        let NUM++
    fi
    sleep 2

done
