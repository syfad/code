#!/bin/bash
#Auth:SunYunfeng
#date:20161020
#nginx 日志分析
#LOG=/dmdata/logs/openresty/api.6clue.com_access_openresty.log 
LOG=$1
#echo "计算访问前10的IP"
topip=`awk '{print $1}' $LOG | sort | uniq -c | sort -nr | head -10`
#awk '{print $1}' $LOG | sort | uniq -c | sort -nr | wc -l
#echo "计算访问前10的时间点"
toptime=`awk '{print $3}' $LOG | cut -c 14,18 | sort | uniq -c | sort -nr | head -10`
#计算访问前10的访问页面
toppage=`awk '{print $7}' $LOG | sort |uniq -c | sort -rn | head -10`
#占用的带宽
total_bandwidth=`awk -v total=0 '{total+=$9}END{print total/1024/1024}' ${LOG}`
#独立用户数
total_unique=`awk '{ip[$1]++}END{print asort(ip)}' ${LOG}`
#PV点击
total_visit=`wc -l ${LOG} | awk '{print $1}'`

echo -e "PV次数: $total_visit"
echo -e "独立用户数: $total_unique"
echo -e "总流量带宽: $total_bandwidth\n"
echo -e "访问前10的IP\n$topip\n"
echo -e "访问集中的时间点\n$toptime\n"
echo -e "访问前10的页面\n$toppage\n"
