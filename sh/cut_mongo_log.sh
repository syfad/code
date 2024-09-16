#!/bin/bash
#AUTH:SunYunfeng
#20160926

LOGPATH=/dmdata/logs/mongodb_20301

pid=`ps aux | grep mongodb  | grep -v grep | awk '{print $2}' | sed -n '1p'`
/bin/kill -SIGUSR1 $pid

