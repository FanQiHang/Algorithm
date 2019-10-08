# -*-coding:utf-8 -*-
# @Time :2019/8/714:49
# @Author : liupengrui
# @FileName :dp_zchwc1.py

# 利用马拉车算法求解
# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/


def longestPalindrome(s):
    if len(s) <= 1:
        return s

    ss = '$#' + '#'.join([x for x in s]) + '#^'  # 首位的特殊字符添加不相同的
    p = [0] * len(ss)

    center = 0
    mx = 0
    max_str = ''

    for i in range(1, len(p) - 1):  # 不包含边界$

        if i < mx:
            p[i] = min(mx - i, 2 * center - i)

        # 尝试继续向两边扩展，更新 p[i]
        while ss[i - p[i] - 1] == ss[i + p[i] + 1]:
            p[i] += 1

        # 中心是需要不断更新的
        if i + p[i] > mx:
            mx = i + p[i]
            center = i

        # 更新最长串，当前求出的长度和上一个状态的比较
        if 1 + 2 * p[i] > len(max_str):
            max_str = ss[i - p[i]: i + p[i] + 1]

    return max_str.replace('#', '')
