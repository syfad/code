#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

import random

def random_list(n):
    ids = list(range(1001,1001+n))

    name1 = ['赵','钱', '孙', '李']
    name2 = ['云', '叶', '勤']
    name3 = ['虎', '龙', '风', '德']

    for i in range(n):
        age = random.randint(18, 60)
        id = ids[i]
        name = random.choice(name1)+random.choice(name2)+random.choice(name3)
        print(id,age,name)


random_list(100)