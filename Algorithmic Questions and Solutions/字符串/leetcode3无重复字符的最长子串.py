# -*- encoding: utf-8 -*-
"""
@File    : test03.py
@Time    : 2019/8/6 13:03
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""


# 未使用滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        res = 0
        for i in range(len(s) - 1):
            ls = [s[i]]
            flag = False
            for j in range(i + 1, len(s)):
                if not s[j] in ls:
                    ls.append(s[j])
                else:
                    flag = True
                res = max(res, len(ls))
                if flag:
                    break
        return res


s = input()

window = []  # 滑动窗口数组
max_length = 0  # 最长串长度

# 遍历字符串
for c in s:
    # 如果字符不在滑动窗口中，则直接扩展窗口
    if c not in window:
        # 使用当前字符扩展窗口
        window.append(c)
    # 如果字符在滑动窗口中，则
    # 1. 从窗口中移除重复字符及之前的字符串部分
    # 2. 再扩展窗口
    else:
        # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
        window[:] = window[window.index(c) + 1:]
        print(window)
        # 扩展窗口
        window.append(c)
        print(window)

    # 更新最大长度
    max_length = max(len(window), max_length)

print(max_length)


