# -*- encoding: utf-8 -*-
"""
@File    : 11.py
@Time    : 2019/9/18 16:38
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""
N = int(input())
l = []
h = []
for i in range(N):
    ls = list(map(int, input().split()))
    l.append(ls[0])
    h.append(ls[1])
ans = 0
i = 0
temp = 0
while i < N:
    if l[i] >= h[i]:
        ans += l[i]
        temp = l[i]  # 最后一个
        i = i + 1
    elif l[i] < h[i]:
        if temp + l[i] < h[i]:
            ans = ans + h[i] - temp
            temp = 0
            i = i + 1
        else:
            ans += l[i]
            temp = l[i]  # 最后一个
            i = i + 1
print(ans)
