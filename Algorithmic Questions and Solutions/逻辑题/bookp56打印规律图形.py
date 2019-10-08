# -*-coding:utf-8 -*-
# @Time :2019/8/611:01
# @Author : liupengrui
# @FileName :bookp56.py

n = int(input())
k = 1
ls = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n - i):
        ls[i + j][j] = k
        k = k + 1

for i in range(n):
    for j in range(i + 1):
        print(ls[i][j], end=' ')
    print()
