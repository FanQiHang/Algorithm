# -*- encoding: utf-8 -*-
"""
@File    : test1.py
@Time    : 2019/6/23 21:50
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""
import pandas as pd

import d2lzh as d2l


def get_max(ls):
    ls = list(map(str, ls))
    ls_sp = []
    for item in ls:
        temp = []
        for i in item:
            temp.append(i)
        ls_sp.append(temp)
    for i in range(0, len(ls_sp) - 1):  # 3 30 34 5 1
        for j in range(0, len(ls_sp) - 1 - i):
            a = ls_sp[j] + ls_sp[j + 1]
            b = ls_sp[j + 1] + ls_sp[j]
            if a < b:
                ls_sp[j], ls_sp[j + 1] = ls_sp[j + 1], ls_sp[j]
        print(ls_sp)
    return ls_sp


if __name__ == '__main__':
    x = get_max([3, 30, 34, 5, 1])
    print(x)
    s = x[0]
    for i in x[1:]:
        x[0].extend(i)
    print('gg', ''.join(x[0]))
