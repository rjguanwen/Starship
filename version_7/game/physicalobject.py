# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     physicalobject
   Description : 游戏对象的超类
   Author :       zhengbin
   date：          2019/11/11
-------------------------------------------------
   Change Activity:
                   2019/11/11:
-------------------------------------------------
"""

__author__ = 'zhengbin <rjguanwen001@163.com>'

import pyglet
from version_7.game import util
from version_7.setting import *

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.dead = False
        # 存放由本对象产生的新对象，例如飞船发射子弹
        self.new_objects = []
        # 是否针对子弹做出响应
        self.reacts_to_bullets = True
        # 是否是子弹
        self.is_bullet = False

        # 键盘与鼠标时间句柄
        self.event_handlers = []

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        # 检查是否超出边界
        self.check_bounds()

    def check_bounds(self):
        """ 检查物体是不是超出的边界，如果超出则从另一侧出来 """
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = WIN_WIDTH + self.image.width / 2
        max_y = WIN_HEIGHT + self.image.height / 2
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
        if not self.reacts_to_bullets and other_object.is_bullet:
            # 如果碰撞物是子弹且本物体不需要响应子弹的碰撞
            return False
        if self.is_bullet and not other_object.reacts_to_bullets:
            return False
        # 计算距离，检测是否碰撞
        # collision_distance = self.image.width * self.scale / 2 + other_object.image.width * self.scale / 2
        collision_distance = self.width / 2 + other_object.width / 2
        actual_distance = util.distance(self.position, other_object.position)
        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        """ 碰撞导致的效果 """
        if other_object.__class__ == self.__class__:
            # 两个相同的物体碰撞不消失，例如两个小行星或者两个子弹
            self.dead = False
        else:
            self.dead = True
