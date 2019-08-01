#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


#线性查找
def linear_search(data_set, value):
    for i in range(len(data_set)):
        if data_set[i] == value:
            return i
    return


#二分查找
def bin_search(data_set, value):
    low = 0
    high = len(data_set) -1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return