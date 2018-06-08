#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng
# @Disc    : support python 2.x and 3.x

from status_monitor import QueryDBs
import sys

def buffer(code):
    query_sql = 'select VARIABLE_VALUE from information_schema.GLOBAL_STATUS where VARIABLE_NAME= "%s"' % code
    query_result = QueryDBs(query_sql)
    print(query_result[0][0])

# total_buffer = int(buffer('Innodb_buffer_pool_pages_total'))
# free_buffer = int(buffer('Innodb_buffer_pool_pages_free'))
# use_buffer = total_buffer - free_buffer
# use_percent = use_buffer / total_buffer

if __name__ == '__main__':
    buffer(sys.argv[1])
