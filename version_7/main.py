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
from pyglet.gl import glClearColor
from version_7.game import load, player, asteroid
from version_7.setting import *

# 创建窗口
game_window = pyglet.window.Window(WIN_WIDTH, WIN_HEIGHT)

# 批量绘制
main_batch = pyglet.graphics.Batch()

# 使用文字标签
score_label = pyglet.text.Label(text="Score: 0", x=SCORE_LABEL_X, y=SCORE_LABEL_Y, batch=main_batch)
game_label = pyglet.text.Label(text=GAME_NAME,
                                x=GAME_LABEL_X, y=GAME_LABEL_Y, anchor_x='center',
                                batch=main_batch)
# game_over_label 的 y 坐标初始设置为负数，使其不可见
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=WIN_WIDTH/2, y=-WIN_HEIGHT/2, anchor_x='center',
                                    batch=main_batch, font_size=48)

# .......
counter = pyglet.window.FPSDisplay(window=game_window)

player_ship = None
player_lives = []
score = 0
num_asteroids = ASTEROIDS_INIT_NUM
game_objects = []

event_stack_size = 0

def init():
    """ 初始化 """
    global score, num_asteroids
    score = 0
    score_label.text = "Score: " + str(score)
    # 小行星个数
    num_asteroids = ASTEROIDS_INIT_NUM
    reset_level(LIVES_NUM)

def reset_level(num_lives):
    """  重置游戏，生命值数是传入参数 """
    global player_ship, player_lives, game_objects, event_stack_size, num_asteroids

    # 清除遗留的事件句柄
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    # 清除右上角显示的生命值图标
    for life in player_lives:
        life.delete()

    # 玩家飞船
    player_ship = player.Player(x=SHIP_INIT_X, y=SHIP_INIT_Y, batch=main_batch)
    # 加载生命值显示
    player_lives = load.player_lives(num_lives, main_batch)
    # 加载小行星
    asteroids = load.asteroids(num_asteroids, player_ship.position, main_batch)

    # 保存游戏对象，用于update
    game_objects = [player_ship] + asteroids

    # 循环所有游戏对象，将各对象的事件句柄压入事件栈
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            # 事件栈计算+1
            event_stack_size += 1

# # 将事件句柄压入事件栈中
# game_window.push_handlers(player_ship.key_handler)
# # 告诉pyglet player_ship是一个事件句柄(event handler)。
# # 用game_window.push_handlers()函数把它压入事件栈中
# game_window.push_handlers(player_ship)

# 装饰器，接管绘制事件。其他事件包括：on_mouse_press, on_key_press
@game_window.event
def on_draw():
    game_window.clear()
    # 背景颜色
    # glClearColor(0.1, 0.6, 1, 1)
    main_batch.draw()

    # .......
    counter.draw()


def update(dt):
    global score, num_asteroids

    # 状态参数
    player_dead = False
    victory = False

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

    # 记录还存在的小行星数量
    asteroids_remaining = 0
    # 更新尚存活的对象，并检查老对象是否生成了新对象
    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        # 将新对象置为空
        obj.new_objects = []
        # 记录小行星个数
        if isinstance(obj, asteroid.Asteroid):
            asteroids_remaining += 1

    # 如果所有小行星都没有了，则游戏胜利
    if asteroids_remaining == 0:
        victory = True

    # 将判断为dead的对象移除
    for to_remove in [obj for obj in game_objects if obj.dead]:

        if to_remove == player_ship:
            player_dead = True

        # 将待 remove 的对象可能存在新对象加入游戏
        to_add.extend(to_remove.new_objects)
        # 移除待 remove 对象
        to_remove.delete()
        game_objects.remove(to_remove)
        # print(to_remove)

        # 如果待移除的是小行星，则记分+1
        if isinstance(to_remove, asteroid.Asteroid):
            score += 1
            score_label.text = "Score: " + str(score)

    # 将新对象置入对象列表
    game_objects.extend(to_add)
    # if len(to_add) > 0:
    #     for o in to_add:
    #         print(o)

    if player_dead:
        # 判断是否还有生命
        if len(player_lives) > 0:
            reset_level(len(player_lives) - 1)
        else:
            game_over_label.y = WIN_HEIGHT / 2
    elif victory:
        # 如果胜利了，则小行星数量+1，记分+10，重新开始游戏
        num_asteroids += 1
        print("num_asteroids: ", num_asteroids)
        player_ship.delete()
        score += 10
        reset_level(len(player_lives))

if __name__ == "__main__":
    # 初始化
    init()
    # 刷新频率设置为每秒120帧
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
