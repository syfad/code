#!/usr/bin/env python
# -*- coding: utf-8 -*-
from inspect import v


def hello():
    print("hello!")

def goodbye():
    print("hello")


if __name__ == '__main__':
    hello()
    goodbye()

#=========求并集=================
a = [1,2,3,4,6,8,10,12]
b = [2,3,4,6,7,10,12,15]
c = [1,2,4,6,7,8,9,11,14]
d = a+b+c
print(set(d))

ccc = []
for i in a:
    for j in b:
        for q in c:
            if i == j == q:
                ccc.append(i)
print(ccc)
ddd=[]
for i in (a+b+c):
    if i not in ccc:
        ddd.append(i)
print(ddd)

print("#=========排序=================")
l1=[1,2,3,4,5,7,9,12]
l2=[1,2,3,4,6,9,14]

# l3=[]
# if l1[0] < l2[0]:
#     l3.append(l1[0])
#     l2.extend(l2)
#     del l2[0]
# else:
#     l3.append(l2[0])
#     l3.extend(l1)
#     del l1[0]
# print(l3)

tmp = []
while len(l1) > 0 and len(l2) > 0:
    if l1[0] < l2[0]:
        tmp.append(l1[0])
        del l1[0]
    else:
        tmp.append(l2[0])
        del l2[0]
tmp.extend(l1)
tmp.extend(l2)
print(tmp)


#===========================
print('#=========装饰器==================')
def count():
    a = 1
    b = 1
    def sum():
        c =1
        return a+c
    print(sum)


import time
def dacorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time-start_time)
    return wrapper

@dacorator

def func():
    time.sleep(0.99)

func()

print('#========计算次数===================')


from collections import Counter
abc = [1,2,454,3,6,3,1,3,5,6,8,4,3,8,4,2,1,2,3,]
counts = Counter(abc)
print(counts)

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

print(all_list(abc))


lists = ['a','a','b',5,6,7,5]
count_dict = dict()
for item in lists:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)


print('#===========================')

a = []
t = [1,2,3,4,6,7,8,10]
s = [1,2,3,4,5,7,9,13]

#t与s的差集
for i in t:
    if i not in s:
        a.append(i)
print("t与s的差集,a:", a)

#s与t的差集
b = []
for i in s:
    if i not in t:
        b.append(i)
print("s与t的差集,b:", b)

#交集
c= []
for i in t:
    if i in s:
        c.append(i)
print("交集,c:", c)

#并集
d = []
for i in (t+s):
    if i not in c:
      d.append(i)
print("并集:", c+d)



print('#===========================')


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_length = len(nums)
        for one_num in range(nums_length - 1):
            for second_num in range(one_num + 1, nums_length):
                if nums[one_num] + nums[second_num] == target:
                    return [one_num, second_num]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(len(nums))
    print(result)
