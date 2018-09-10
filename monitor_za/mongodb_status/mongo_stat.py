#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    :
# @Disc    : support python 2.x and 3.x

from pymongo import MongoClient
import os, sys



class MongoDBPipeline(object):
    def __init__(self,db,col,address,replicaSet):

        # self.db = DB['db']
        # self.col = DB['col']
        # #connection = pymongo.Connection(self.server,self.port)
        # #connection = MongoClient(self.server,self.port)
        # connection = MongoClient(DB['address'], replicaSet=DB['replicaSet'])
        # db = connection[self.db]
        # self.collection = db[self.col]
        #print 'db is ['+db+']'
        self.db = db
        self.col = col
        #connection = pymongo.Connection(self.server,self.port)
        #connection = MongoClient(self.server,self.port)
        connection = MongoClient(address, replicaSet=replicaSet)
        db = connection[self.db]
        self.collection = db[self.col]

    def save(self, item):
        #self.collection.insert_one(dict(item))
        #elf.collection.insert_one(item)
        self.collection.insert_one(item)

        return item

    def find(self, item):

        item = self.collection.find(item).count()
        #print item
        return item

    def aggregate(self, item):
        item = self.collection.aggregate(item)
        return item

# def stats():
#     cli = MongoDBPipeline('192.168.100.186:20301,192.168.100.133:20301', '', 'admin', 'dmmongo')
#     status = cli.rs.status()
#     return status


myclient = MongoClient("mongodb://192.168.100.186:20301/")
cli = myclient['admin']
# print cli.db.serverStatus()
