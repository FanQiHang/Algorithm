# -*-coding:utf-8 -*-
# @Time :2019/7/2521:25
# @Author : liupengrui
# @FileName :train463.py


class Solution(object):

    def islandPerimeter(self, grid):
        count = 0
        count1 = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    count = count + 1

        # 竖着扫描交集
        for i in range(0, len(grid) - 1):
            for j in range(0, len(grid[0])):
                if grid[i][j] and grid[i + 1][j]:
                    count1 = count1 + 1
        # 横着扫描
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0]) - 1):
                if grid[i][j] and grid[i][j + 1]:
                    count1 = count1 + 1

        return 4 * count - 2 * count1
