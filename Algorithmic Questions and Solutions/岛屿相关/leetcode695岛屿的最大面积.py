# -*-coding:utf-8 -*-
# @Time :2019/7/2521:20
# @Author : liupengrui
# @FileName :train695.py


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        x_length = len(grid)
        y_length = len(grid[0])
        vis = [[1 for _ in range(y_length)] for _ in range(x_length)]

        def DFS(i, j, vis=vis):
            if 0 <= i < x_length and 0 <= j < y_length and vis[i][j] == 1 and grid[i][j] == 1:
                vis[i][j] = 0
                res = DFS(i - 1, j) + DFS(i + 1, j) + DFS(i, j - 1) + DFS(i, j + 1) + 1
                # print i,j,res
                return res
            else:
                return 0

        res = [0]
        for i in range(x_length):
            for j in range(y_length):
                if vis[i][j] == 1 and grid[i][j] == 1:
                    val = DFS(i, j, vis=vis)
                    # print i, j, val, vis

                    res.append(val)

        return max(res)


ceshi = Solution()
print(ceshi.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
