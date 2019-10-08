# -*-coding:utf-8 -*-
# @Time :2019/8/209:31
# @Author : liupengrui
# @FileName :0-1bag.py
import numpy as np


# https://www.jianshu.com/p/25f4a183ede5
# https://blog.csdn.net/w113691/article/details/81743201

def solve1(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength + 1, totalWeight + 1), dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(1, totalWeight + 1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i - 1, j - wlist[i]] + vlist[i], resArr[i - 1, j])
            else:
                resArr[i, j] = resArr[i - 1, j]
    return resArr[-1, -1]


def solve2(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros(totalWeight + 1, dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(totalWeight, 0, -1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j], resArr[j - wlist[i]] + vlist[i])
    return resArr[-1]
