# -*-coding:utf-8 -*-
# @Time :2019/7/2521:09
# @Author : liupengrui
# @FileName :test03.py

# 岛屿的个数


class Solution:
    def numIslands(self, grid):
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.dfsfind(grid, i, j, row, col)  # 将连成片的1都改为0之后，返回1个岛屿的数量
                    count += 1
        return count

    def dfsfind(self, grid, i, j, row, col):
        if grid[i][j] == 1:
            grid[i][j] = 0
            if i - 1 >= 0:
                grid = self.dfsfind(grid, i - 1, j, row, col)
            if i + 1 < row:
                grid = self.dfsfind(grid, i + 1, j, row, col)
            if j - 1 >= 0:
                grid = self.dfsfind(grid, i, j - 1, row, col)
            if j + 1 < col:
                grid = self.dfsfind(grid, i, j + 1, row, col)
        return grid


ceshi = Solution()
print(ceshi.numIslands(
    [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
