# -*-coding:utf-8 -*-
# @Time :2019/8/715:11
# @Author : liupengrui
# @FileName :bianjidistance.py


def func(x, y):
    print(len(x), len(y))
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

    for j in range(len(y) + 1):
        dp[0][j] = j

    for i in range(len(x) + 1):
        dp[i][0] = i

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    print(dp)

    print(dp[-1][-1])


func('horse', 'ros')


def minDistance(word1: str, word2: str):
    n1 = len(word1)
    n2 = len(word2)
    print(n1, n2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    # 第一行
    for j in range(n2 + 1):
        dp[0][j] = j
    # 第一列
    for i in range(n1 + 1):
        dp[i][0] = i
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    print(dp)
    print(dp[-1][-1])


minDistance('horse', 'ros')
