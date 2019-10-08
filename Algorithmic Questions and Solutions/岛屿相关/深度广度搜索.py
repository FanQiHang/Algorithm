# -*- encoding: utf-8 -*-
"""
@File    : 深度搜索.py
@Time    : 2019/8/28 10:06
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""


class Solution:

    def numIslands(self, grid):
        mark = [[0] * len(grid[0]) for _ in range(len(grid))]
        islands_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if mark[i][j] == 0 and grid[i][j] == 1:
                    # self.dfs(mark, grid, i, j)
                    self.bfs(mark, grid, i, j)
                    islands_num += 1
        return islands_num

    def dfs(self, mark, grid, x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        mark[x][y] = 1
        for i in range(4):  # 四个方向
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= len(mark) or new_y < 0 or new_y >= len(mark[0]):
                continue
            if mark[new_x][new_y] == 0 and grid[new_x][new_y] == 1:
                self.dfs(mark, grid, new_x, new_y)

    def bfs(self, mark, grid, x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        mark[x][y] = 1
        queen = []
        queen.append([x, y])
        while queen:
            x = queen[0][0]
            y = queen[0][1]
            queen.pop(0)  # 将首部元素弹出
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x < 0 or new_x >= len(mark) or new_y < 0 or new_y >= len(mark[0]):
                    continue
                if mark[new_x][new_y] == 0 and grid[new_x][new_y] == 1:
                    queen.append([new_x, new_y])
                    mark[new_x][new_y] = 1


mm = Solution()
print(mm.numIslands([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1]]))
