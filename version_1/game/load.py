# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     load
   Description :
   Author :       zhengbin
   date：          2019/11/11
-------------------------------------------------
   Change Activity:
                   2019/11/11:
-------------------------------------------------
"""

__author__ = 'zhengbin <rjguanwen001@163.com>'

import math
import pyglet, random
from version_1.game import resources

def asteroids(num_asteroids, player_position):
    """ 加载小行星 """
    asteroids = []
    for i in range(num_asteroids):
        # asteroid_x = random.randint(0, 800)
        # asteroid_y = random.randint(0, 600)
        asteroid_x, asteroid_y = player_position
        # 判断小行星与玩家之间的距离
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)
        # 随机旋转小行星的角度
        new_asteroid.rotation = random.randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids

def distance(point_1=(0, 0), point_2=(0, 0)):
    """ 计算两个点之间的距离 """
    return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
