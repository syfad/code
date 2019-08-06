#!/usr/bin/env python
## -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import random
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        x = func(*args, **kwargs)
        ti2 = time.time()
        print("time cost:", ti2 - ti)
        return x
    return wrapper()




def random_list(n):
    ids = list(range(1001,1001+n))

    name1 = ['赵','钱', '孙', '李']
    name2 = ['云', '叶', '勤']
    name3 = ['虎', '龙', '风', '德']

    for i in range(n):
        age = random.randint(18, 60)
        id = ids[i]
        name = random.choice(name1)+random.choice(name2)+random.choice(name3)
        user_list = [i, id,age,name]
        return user_list
        #print(user_list)
#random_list(100)


#@cal_time
def bin_search(data_set, val):
    low = 0
    high = len(data_set) -1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == val:
            #print(mid)
            return mid
        elif data_set[mid] < val:
            low = mid +1
        else:
            high = mid - 1
    return

# data = list(range(10000))
# print(data)
# #bin_search(data, 100)