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
from version_6.game import load, player
from version_6.setting import *

# 创建窗口
game_window = pyglet.window.Window(WIN_WIDTH, WIN_HEIGHT)

# 批量绘制
main_batch = pyglet.graphics.Batch()

# 使用文字标签
score_label = pyglet.text.Label(text="Score: 0", x=SCORE_LABEL_X, y=SCORE_LABEL_Y, batch=main_batch)
game_label = pyglet.text.Label(text=GAME_NAME,
                                x=GAME_LABEL_X, y=GAME_LABEL_Y, anchor_x='center',
                                batch=main_batch)

# 玩家飞船
player_ship = player.Player(x=SHIP_INIT_X, y=SHIP_INIT_Y, batch=main_batch)
# 加载小行星
asteroids = load.asteroids(ASTEROIDS_INIT_NUM, player_ship.position, main_batch)

# 加载生命值显示
player_lives = load.player_lives(LIVES_NUM, main_batch)

# 保存游戏对象，用于update
game_objects = [player_ship] + asteroids


# 将事件句柄压入事件栈中
game_window.push_handlers(player_ship.key_handler)
# 告诉pyglet player_ship是一个事件句柄(event handler)。
# 用game_window.push_handlers()函数把它压入事件栈中
game_window.push_handlers(player_ship)

# 装饰器，接管绘制事件。其他事件包括：on_mouse_press, on_key_press
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    # 循环所有对象，两两进行碰撞判断
    for i in range(len(game_objects)):
        for j in range(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    # 定义数组，用来暂存老对象生成的新对象
    to_add = []
    # 更新尚存活的对象，并检查老对象是否生成了新对象
    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        # 将新对象置为空
        obj.new_objects = []
    # 将新对象置入对象列表
    game_objects.extend(to_add)
    # if len(to_add) > 0:
    #     for o in to_add:
    #         print(o)

    # 将判断为dead的对象移除
    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        game_objects.remove(to_remove)
        # print(to_remove)


if __name__ == "__main__":
    # 刷新频率设置为每秒120帧
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
