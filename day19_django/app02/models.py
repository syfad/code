# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    #id列,自增，主键,默认会自己创建一列id
    #用户列，字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)