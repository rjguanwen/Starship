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
from version_5.game import physicalobject, resources, bullet

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
        # 子弹初始速度
        self.bullet_speed = 700.0

        self.reacts_to_bullets = False

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
            if self.velocity_x > 300:
                self.velocity_x = 300
            if self.velocity_y >300:
                self.velocity_y =300

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

    # 按下空格键时开火发射子弹
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    # 发射子弹
    def fire(self):
        # 将角度转换为弧度并逆转方向
        angle_radians = -math.radians(self.rotation)
        # 计算子弹位置并实例化
        ship_radius = self.image.width / 2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
        # 计算子弹速度，与计算飞船速度类似
        bullet_vx = (self.velocity_x + math.cos(angle_radians) * self.bullet_speed)
        bullet_vy = (self.velocity_y + math.sin(angle_radians) * self.bullet_speed)
        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy
        # 将子弹加入对象列表
        self.new_objects.append(new_bullet)

    def handle_collision_with(self, obj2):
        """ 碰撞之后的动作 """
        # if isinstance(obj2, bullet.Bullet):
        #     # 如果飞船是与子弹相碰
        #     pass
        # else:
        #     # 否则飞船被销毁
        #     self.dead = True
        self.dead = True