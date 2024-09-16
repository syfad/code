#!/usr/bin/env python
# -*- coding: utf-8 -*-
#随机四位验证码

import random_num

checkcode=''

for i in range(4):
    current=random_num.randint(1, 9)
    checkcode+=str(current)
print (checkcode)