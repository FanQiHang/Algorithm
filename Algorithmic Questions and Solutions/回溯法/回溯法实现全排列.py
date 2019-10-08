# -*-coding:utf-8 -*-
# @Time :2019/8/815:07
# @Author : liupengrui
# @FileName :quanpailie.py

class Solution:

    def permute(self, nums):

        if len(nums) == 0:
            return []
        used = [False] * len(nums)  # 用来记录当前位置的数是否已经使用过
        index = 0  # 用于判断递归是否终止，终止后返回最底层的一个结果
        res = []
        print('ii')
        self.__dfs(nums, index, [], used, res)
        print('iii')
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


mm = Solution()
n = int(input())

print(mm.permute([1, 2, 3]))
