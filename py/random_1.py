#!/usr/bin/env python
# -*- coding: utf8 -*-


# from random import randint
# import sys
#
# num = randint(1, 10)
#
# print "guess what i think"
# while True:
#     bingin = input()
#
#     if bingin > num:
#         print 'too big'
#
#     if bingin < num:
#         print "too small"
#
#     if bingin == num:
#         print "BINGO"
#         sys.exit(1)

for i in range(0, 5):
    for j in range(0, i+1):
        print '*'
    print