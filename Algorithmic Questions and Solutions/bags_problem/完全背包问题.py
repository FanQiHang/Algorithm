# -*-coding:utf-8 -*-
# @Time :2019/8/209:34
# @Author : liupengrui
# @FileName :total.py

# https://www.jianshu.com/p/7a4e6071bc02
import numpy as np


def solve3(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros(totalWeight + 1, dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(1, totalWeight + 1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j], resArr[j - wlist[i]] + vlist[i])
    return resArr[-1]
