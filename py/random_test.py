#!/usr/bin/env python
# -*- coding: utf-8 -*-
#随机四位验证码

import random

checkcode=''

for i in range(4):
    current=random.randint(1,9)
    checkcode+=str(current)
print (checkcode)