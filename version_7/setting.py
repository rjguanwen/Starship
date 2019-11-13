# -*- coding: utf-8 -*-
# Copyright (c) 2019 - zhengbin <rjguanwen001@163.com>
# Create Date: 2019/11/12

""" 全局设置 """

import sys

GAME_NAME = "星际飞船大作战"
# 窗口宽度与高度
WIN_WIDTH, WIN_HEIGHT = 1000, 800
# 记分与游戏标题的位置
SCORE_LABEL_X, SCORE_LABEL_Y = 10, WIN_HEIGHT - 25
GAME_LABEL_X, GAME_LABEL_Y = WIN_WIDTH / 2, SCORE_LABEL_Y
# 飞船初始化的位置
SHIP_INIT_X, SHIP_INIT_Y = WIN_WIDTH / 2, WIN_HEIGHT / 2
# 起始小行星个数
ASTEROIDS_INIT_NUM = 1
# 生命值，生命值以小图标的个数表示，因此不能过大
LIVES_NUM = 6
LIVES_ICON_X, LIVES_ICON_Y = WIN_WIDTH - 15, WIN_HEIGHT - 15
# 飞船在x、y方向的最大速度，设为-1表示不限制
SHIP_MAX_VELOCITY_X, SHIP_MAX_VELOCITY_Y = 300.0, 300.0
# 飞船推力
SHIP_THRUST = 300.0
#飞船旋转速度
SHIP_TOTATE_SPEED = 200.0
# 子弹初速度
BULLET_SPEED = 700.0


