# -*-coding:utf-8 -*-
# @Time :2019/8/1317:20
# @Author : liupengrui
# @FileName :fanzhuan_char.py

s = "a good   example mm"
ls = s.split(' ')
for i in range(len(ls) - 1, -1, -1):
    print(ls)
    if ls[i] == '':
        ls.remove('')

if len(ls) % 2 != 0:
    mid = len(ls) // 2
    for i in range(mid):
        ls[i], ls[2 * mid - i] = ls[2 * mid - i], ls[i]
else:
    mid = len(ls) // 2
    for i in range(mid):
        ls[i], ls[2 * mid - i - 1] = ls[2 * mid - i - 1], ls[i]

print(ls)
