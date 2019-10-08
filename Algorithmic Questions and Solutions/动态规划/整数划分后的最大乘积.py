# -*- encoding: utf-8 -*-
"""
@File    : max_chengji.py
@Time    : 2019/8/6 17:14
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""


# 将整数进行划分，找到最大的乘积
# 使用动态规划，自底向上求解，一般递归树形结构都可以尝试利用动态规划自底向上求解

def func(n):
    # 先定义一个list存储中间结果（当前的最大乘积）
    ls = [1] * (n + 1)
    for i in range(2, n + 1):
        for j in range(i - 1, 1, -1):
            ls[i] = max(ls[i], (i - j) * j, ls[i - j] * j)
    return max(ls), ls


print(func(10))
