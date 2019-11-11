# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     player
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
import pyglet
from pyglet.window import key
from version_4.game import physicalobject, resources


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image,
                                     *args, **kwargs)
        # 飞船的推力
        self.thrust = 300.0
        # 飞船的旋转速度
        self.rotate_speed = 200.0
        # 使用 pyglet.window.key.KeyStateHandler自动跟踪按键状态
        self.key_handler = key.KeyStateHandler()
        # 引擎火焰初始化
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image,
                                                  *args, **kwargs)
        # 火焰初始不可见
        self.engine_sprite.visible = False

    def update(self, dt):
        super(Player, self).update(dt)
        self.move_mode_1(dt)

    def move_mode_1(self, dt):
        if self.key_handler[key.LEFT]:
            # 如果按下left键，则飞船向左旋转
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            # 如果按下right键，则飞船向右旋转
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            # 如果按下up键，则飞船前进
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            # up键按下，引擎发动，引擎火焰出现
            # 设置引擎火焰的位置与显示
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            #
            self.engine_sprite.visible = False


    def move_mode_2(self, dt):
        if self.key_handler[key.LEFT]:
            # 如果按下left键，则飞船向左飞
            self.x -= self.thrust * dt
        if self.key_handler[key.RIGHT]:
            # 如果按下right键，则飞船向右旋转
            self.x += self.thrust * dt
        if self.key_handler[key.UP]:
            # 如果按下up键，则飞船前进
            self.y += self.thrust * dt
        if self.key_handler[key.DOWN]:
            # 如果按下down键，则飞船后退
            self.y -= self.thrust * dt

    def delete(self):
        """ 销毁 """
        #  删除引擎火焰
        self.engine_sprite.delete()
        # 删除飞船
        super(Player, self).delete()