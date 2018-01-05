#!/bin/sh 
# Ping网段所有IP 
ip="192.168.100." 
for i in `seq 1 254` 
do 
ping -c 2 $ip$i | grep -q 'ttl=' && echo "$ip$i yes"|| echo "$ip$i no" 
#yes正常，no主机不存在或不正常 
done 
