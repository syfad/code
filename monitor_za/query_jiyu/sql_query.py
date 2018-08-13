#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-02
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import querysql
import pymysql
#import config
import time
import datetime
#from db import MongoDBPipeline
from pymongo import MongoClient




def user_num():
    sql = 'select count(*) from space.members'
    num = querysql.QueryDBs(sql)
    print num[0][0]


user_num()