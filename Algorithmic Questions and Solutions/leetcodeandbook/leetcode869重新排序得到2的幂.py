# -*-coding:utf-8 -*-
# @Time :2019/8/922:22
# @Author : liupengrui
# @FileName :leetcode869.py

import collections
import random

#
# random.shuffle()

a = [1, 2, 3, 4, 5]
# for i in range(len(a) - 1):
#     j = random.randint(0, len(a) - 1 - i)  # i+j<=len(a)-1
#     a[i], a[i + j] = a[i + j], a[i]
# print(a)

for i in reversed(range(1, len(a))):
    # pick an element in x[:i+1] with which to exchange x[i]
    j = int(random.random() * (i + 1))
    a[i], a[j] = a[j], a[i]
print(a)


def dajiang01():
    n, m = list(map(int, input().split(' ')))
    lsA = ['A'] * n
    lsB = ['B'] * m
    if 3 * n < m or 3 * m < n:
        print('不满足')
    else:
        lsA.extend(lsB)
        while True:
            global flag
            flag = True

            random.shuffle(lsA)

            # for i in range(len(a) - 1):
            #     j = random.randint(0, len(a) - 1 - i)  # i+j<=len(a)-1
            #     lsA[i], lsA[i + j] = lsA[i + j], lsA[i]

            # for i in reversed(range(1, len(lsA))):
            #     j = int(random.random() * (i + 1))
            #     lsA[i], lsA[j] = lsA[j], lsA[i]

            for j in range(1, len(lsA) - 1):
                if lsA[j - 1] == lsA[j] == lsA[j + 1]:
                    flag = False
                    break
            print('ii')
            if flag:
                print(lsA)
                return


dajiang01()
exit()


def reorderedPowerOf2(N):
    m = collections.Counter(str(N))

    n = len(str(N))  # 传入821，n=3

    num = 1
    while len(str(num)) < n:
        num *= 2

    while len(str(num)) == n:  # 判断等长度
        if collections.Counter(str(num)) == m:  # m输入821，可以排列得到128
            return True
        num *= 2
    return False


N = int(input())
print(reorderedPowerOf2(N))


# 使用递归方法判断整数数组是否为递增序列
def fun(a, n):
    if n == 1:
        return True
    if n == 2:
        return a[n - 1] >= a[n - 2]
    return fun(a, n - 1) and (a[n - 1] >= a[n - 2])
