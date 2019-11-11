# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     resources
   Description : 操作资源文件
   Author :       zhengbin
   date：          2019/11/11
-------------------------------------------------
   Change Activity:
                   2019/11/11:
-------------------------------------------------
"""

__author__ = 'zhengbin <rjguanwen001@163.com>'

import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

def center_image(image):
    """ 通过设置图片锚点使其居中 """
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# 加载图片
player_image = pyglet.resource.image('player.png')
bullet_image = pyglet.resource.image('bullet.png')
asteroid_image = pyglet.resource.image('asteroid.png')
# 使图片锚点居中
center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)