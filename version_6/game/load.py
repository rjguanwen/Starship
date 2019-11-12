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
from version_6.game import resources, asteroid, util
from version_6.setting import *

def asteroids(num_asteroids, player_position, batch=None):
    """ 加载小行星 """
    asteroids = []
    for i in range(num_asteroids):
        # asteroid_x = random.randint(0, 800)
        # asteroid_y = random.randint(0, 600)
        asteroid_x, asteroid_y = player_position
        # 判断小行星与玩家之间的距离
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, WIN_WIDTH)
            asteroid_y = random.randint(0, WIN_HEIGHT)
        # 生成小行星
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        # 随机旋转小行星的角度
        new_asteroid.rotation = random.randint(0, 360)
        # 为小行星设置随机速度
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
        asteroids.append(new_asteroid)
    return asteroids

def player_lives(num_icons, batch=None):
    """ 绘制一排小图标，用来表示剩余生命数 """
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=LIVES_ICON_X-i*30, y=LIVES_ICON_Y,
                                          batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives