# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     util.py
   Description : 一些工具方法
   Author :       zhengbin
   date：          2019/11/11
-------------------------------------------------
   Change Activity:
                   2019/11/11:
-------------------------------------------------
"""

__author__ = 'zhengbin <rjguanwen001@163.com>'

import math


def distance(point_1=(0, 0), point_2=(0, 0)):
    """ 计算两个点之间的距离 """
    return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
