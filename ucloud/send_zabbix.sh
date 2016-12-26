#!/bin/bash

Sendpath=/usr/local/zabbix_agent/bin/zabbix_sender
Command=`/usr/bin/python /usr/local/zabbix_agent/scripts/ucloud/ucloud.py`
Zabbix_host=172.16.0.121


$Sendpath -z $Zabbix_host -p 10051 -s "Solr-109" -k refreshcdn -o $Command

