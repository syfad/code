#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x


import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)

from core import src

if __name__ == '__main__':
    src.run()