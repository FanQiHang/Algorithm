# -*-coding:utf-8 -*-
# @Time :2019/8/615:33
# @Author : liupengrui
# @FileName :bookp60.py

# 划分整数


def divinteger(n, m):
    if n == 1 or m == 1:
        return 1
    elif n < m:
        return divinteger(n, n)
    elif n == m:
        return 1 + divinteger(n, n - 1)
    return divinteger(n, m - 1) + divinteger(n - m, m)


print(divinteger(58, 58))
