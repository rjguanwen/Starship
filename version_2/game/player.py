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
from pyglet.window import key
from version_2.game import physicalobject, resources

class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image,
                                     *args, **kwargs)
        # 飞船的推力
        self.thrust = 300.0
        # 飞船的旋转速度
        self.rotate_speed = 200.0
        # 按键字典
        self.keys = dict(left=False, right=False, up=False, down=False)

    def on_key_press(self, symbol, modifiers):
        """ 捕获键盘被按下事件 """
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        """ 捕获按键被释放事件 """
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False

    def update(self, dt):
        super(Player, self).update(dt)
        self.move_mode_2(dt)

    def move_mode_1(self, dt):
        if self.keys['left']:
            # 如果按下left键，则飞船向左旋转
            self.rotation -= self.rotate_speed * dt
        if self.keys['right']:
            # 如果按下right键，则飞船向右旋转
            self.rotation += self.rotate_speed * dt
        if self.keys['up']:
            # 如果按下up键，则飞船前进
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
        if self.keys['down']:
            # 如果按下up键，则飞船前进
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x -= force_x
            self.velocity_y -= force_y

    def move_mode_2(self, dt):
        if self.keys['left']:
            # 如果按下left键，则飞船向左飞
            self.x -= self.thrust * dt
        if self.keys['right']:
            # 如果按下right键，则飞船向右旋转
            self.x += self.thrust * dt
        if self.keys['up']:
            # 如果按下up键，则飞船前进
            self.y += self.thrust * dt
        if self.keys['down']:
            # 如果按下up键，则飞船前进
            self.y -= self.thrust * dt


