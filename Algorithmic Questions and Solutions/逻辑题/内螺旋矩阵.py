# -*- encoding: utf-8 -*-
"""
@File    : test04.py
@Time    : 2019/7/31 23:39
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""


# 内螺旋矩阵
def interSpiralMatrix(size):
    if size % 2 != 1:  # size必须是奇数
        size += 1
    spiralMatrix = [([0] * size) for i in range(size)]  # 生成矩阵
    x, y, side = int(size / 2), int(size / 2), size - 1
    print(x, y, side)
    for i in range(1, size ** 2 + 1):  # 坐标的变化是 x++ , y ++, x--, y--,,,i 表示所有的值
        spiralMatrix[y][x] = i
        if y <= -x + side and y <= x:  # 划分四个区域，然后就是通过直线来分开
            x += 1
        elif -x + side < y and y < x:
            y += 1
        elif x <= y and -x + side < y:
            x -= 1
        elif x < y and y <= -x + side:
            y -= 1
    for matrix in spiralMatrix:
        print("\t".join(map(lambda x: str(x), matrix)))

interSpiralMatrix(5)
