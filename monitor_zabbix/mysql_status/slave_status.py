#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng
# @Disc    : support python 2.x and 3.x

from status_monitor import QueryDBs
import sys

def slave(code):
    query_sql = 'show slave status'
    query_result = QueryDBs(query_sql)
    print(query_result)



