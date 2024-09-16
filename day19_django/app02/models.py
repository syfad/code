# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    #id列,自增，主键,默认会自己创建一列id
    #用户列，字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class Business(models.Model):
    #id
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,default='SA')#default 为默认字符



class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id', on_delete=1)#外键关联到Business表

