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
from version_6.game import physicalobject, resources, player


class Bullet(physicalobject.PhysicalObject):
    """ 子弹 """

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(
            resources.bullet_image,
            *args,
            **kwargs
        )
        # 0.5秒后调用一次 die 方法
        pyglet.clock.schedule_once(self.die, 1)
        # 标记自己是子弹
        self.is_bullet = True

    # 子弹从屏幕消失
    def die(self, dt):
        self.dead = True

    def handle_collision_with(self, obj2):
        """ 碰撞之后的动作 """
        # if isinstance(obj2, player.Player):
        #     # 如果飞船是与子弹相碰
        #     pass
        # else:
        #     self.dead = True
        self.dead = True