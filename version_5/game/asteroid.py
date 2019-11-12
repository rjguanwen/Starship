# -*- coding: utf-8 -*-
# Copyright (c) 2019 - zhengbin <rjguanwen001@163.com>
# Create Date: 2019/11/12

""" 小行星 """

import pyglet
import random
from version_5.game import resources, physicalobject

class Asteroid(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(resources.asteroid_image, *args, **kwargs)
        # 为小行星增加旋转速度
        self.rotate_speed = random.random() * 100.0 - 50.0

    def handle_collision_with(self, other_object):
        """ 覆写碰撞事件，碰撞后不消失，而是碎裂为更小的 """
        super(Asteroid, self).handle_collision_with(other_object)
        if self.dead and self.scale > 0.25:
            # 生成2到4个小行星
            num_asteroids = random.randint(2, 4)
            # 循环生成每个小行星，随机方向与速度，大小减半
            for i in range(num_asteroids):
                 new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                 new_asteroid.rotation = random.randint(0, 360)
                 new_asteroid.velocity_x = random.random() * 70 + self.velocity_x
                 new_asteroid.velocity_y = random.random() * 70 + self.velocity_y
                 new_asteroid.scale = self.scale * 0.5
                 self.new_objects.append(new_asteroid)

    def update(self, dt):
        """ 覆写 update 方法，增加小行星的旋转 """
        super(Asteroid, self).update(dt)
        self.rotation += self.rotate_speed * dt
