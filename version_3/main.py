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
from version_3.game import load, physicalobject, player, resources

# 创建窗口
game_window = pyglet.window.Window(800, 600)

# 批量绘制
main_batch = pyglet.graphics.Batch()

# 使用文字标签
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=400, y=575, anchor_x='center',
                                batch=main_batch)

# 玩家飞船
player_ship = player.Player(x=400, y=300, batch=main_batch)
# 加载小行星
asteroids = load.asteroids(6, player_ship.position, main_batch)

# 加载生命值显示
player_lives = load.player_lives(5, main_batch)


# 装饰器，接管绘制事件。其他事件包括：on_mouse_press, on_key_press
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

# 保存游戏对象，用于update
game_objects = [player_ship] + asteroids
def update(dt):
    for obj in game_objects:
        obj.update(dt)

# 告诉pyglet player_ship是一个事件句柄(event handler)。
# 用game_window.push_handlers()函数把它压入事件栈中
game_window.push_handlers(player_ship.key_handler)

if __name__ == "__main__":

    # 刷新频率设置为每秒120帧
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()