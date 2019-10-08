# -*-coding:utf-8 -*-
# @Time :2019/8/79:14
# @Author : liupengrui
# @FileName :dp_zchwc.py

# 使用动态规划求最长回文串


def func(s):
    le = len(s)
    if le <= 1:
        return s
    # 构造一个二维list
    dp = [[0 for i in range(le)] for j in range(le)]
    max = 1
    start = 0
    for j in range(le):
        for i in range(j, -1, -1):  # 循环的顺序需要注意
            if i == j:
                dp[i][j] = 1
            elif j - i == 1:
                if s[i] == s[j]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 0
            elif j - i >= 2:
                if s[i] == s[j]:
                    if dp[i + 1][j - 1] > 0:  # 去头去尾是回文串
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = 0
            print(dp[i][j])
            if dp[i][j] > max:
                max = dp[i][j]
                start = i
    print(start, max)
    return s[start:start + max]


print(func('google'))
