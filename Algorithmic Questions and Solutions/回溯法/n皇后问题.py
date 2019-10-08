# -*-coding:utf-8 -*-
# @Time :2019/8/816:32
# @Author : liupengrui
# @FileName :n_queen.py


class Solution:
    def solveNQueens(self, n):
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])  # 只要可以对应到某个位置即可

        def place_queen(row, col):
            queens.add((row, col))  # 加入可以放置的位置
            cols[col] = 1  # 表示占领
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0  # 表示释放
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):  # 遍历所有列
                if could_place(row, col):  # 如果满足可以放置的条件
                    place_queen(row, col)  # 进行放置
                    if row + 1 == n:  # 如果所有行都遍历过了，则返回解决方案
                        add_solution()
                    else:  # 如果没有，则继续遍历
                        backtrack(row + 1)
                    remove_queen(row, col)  # 释放位置

        cols = [0] * n  # 列
        hill_diagonals = [0] * (2 * n - 1)  # 次对角线
        dale_diagonals = [0] * (2 * n - 1)  # 主对角线
        queens = set()
        output = []
        backtrack()
        return output


mm = Solution()
xx = mm.solveNQueens(4)
print(xx)
