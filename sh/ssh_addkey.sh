#!/bin/sh
#结合expect脚本实现
. /etc/init.d/functions
for ip in `cat ip.txt`
do
    expect  ssh_addhost.exp ~/.ssh/id_rsa.pub $ip >/dev/null 2>&1
    if [ $? -eq 0 ];then
       action "$ip" /bin/true
    else
       action "$ip" /bin/false
    fi
done
