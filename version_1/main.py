# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description : 程序主入口
   Author :       zhengbin
   date：          2019/11/11
-------------------------------------------------
   Change Activity:
                   2019/11/11:
-------------------------------------------------
"""

__author__ = 'zhengbin <rjguanwen001@163.com>'

import pyglet
from version_1.game import resources, load

# 创建窗口
game_window = pyglet.window.Window(800, 600)


# 使用文字标签
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=400, y=575, anchor_x='center')

# 玩家飞船
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
# 加载小行星
asteroids = load.asteroids(6, player_ship.position)

# 装饰器，接管绘制事件。其他事件包括：on_mouse_press, on_key_press
@game_window.event
def on_draw():
    game_window.clear()
    # 绘制级别与分数的文字标签
    level_label.draw()
    score_label.draw()
    # 绘制飞船
    player_ship.draw()
    # 绘制小行星
    for asteroid in asteroids:
        asteroid.draw()

if __name__ == "__main__":
    pyglet.app.run()