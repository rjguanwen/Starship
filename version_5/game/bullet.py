# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     bullet
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
from version_5.game import physicalobject, resources


class Bullet(physicalobject.PhysicalObject):
    """ 子弹 """

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(
            resources.bullet_image,
            *args,
            **kwargs
        )
        # 0.5秒后调用一次 die 方法
        pyglet.clock.schedule_once(self.die, 0.5)

    # 子弹从屏幕消失
    def die(self, dt):
        self.dead = True