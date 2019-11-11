# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     physicalobject
   Description :
   Author :       zhengbin
   date：          2019/11/11
-------------------------------------------------
   Change Activity:
                   2019/11/11:
-------------------------------------------------
"""

__author__ = 'zhengbin <rjguanwen001@163.com>'

import pyglet
from version_4.game import util

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.dead = False

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        # 检查是否超出边界
        self.check_bounds()

    def check_bounds(self):
        """ 检查物体是不是超出的边界，如果超出则从另一侧出来 """
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y


    def collides_with(self, other_object):
        """ 判断两个物体是否碰撞 """
        collision_distance = self.image.width / 2 + other_object.image.width / 2
        actual_distance = util.distance(self.position, other_object.position)
        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        """ 碰撞导致的效果 """
        self.dead = True
