# -*- encoding: utf-8 -*-
"""
@File    : test08.py
@Time    : 2019/8/3 15:53
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""


# 回溯法实现全排列
class Solution:

    def permute(self, nums):

        if len(nums) == 0:
            return []
        used = [False] * len(nums)  # 用来记录当前位置的数是否已经使用过
        index = 0  # 用于判断递归是否终止，终止后返回最底层的一个结果
        res = []

        self.__dfs(nums, index, [], used, res)

        return res

    def __dfs(self, nums, index, per, used, res):

        if index == len(nums):
            res.append(per.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                per.append(nums[i])

                self.__dfs(nums, index + 1, per, used, res)

                # 释放当前位置
                used[i] = False
                # 释放当前的数
                per.pop()
