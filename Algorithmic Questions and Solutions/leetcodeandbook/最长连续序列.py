# -*-coding:utf-8 -*-
# @Time :2019/8/520:23
# @Author : liupengrui
# @FileName :zuichanglxxl.py

# 找到最长的连续序列

ls_data = [100, 1, 4, 200, 1, 3, 2, 6, 7, 8, 9, 10]
ls_res = []
ls = []
res = 0
for i in range(1000):
    if i + 1 in ls_data:
        ls.append(i + 1)
    else:
        if len(ls) != 0 and res < len(ls):
            ls_res = ls  # 直接赋值
            res = len(ls)
        ls = []
print(ls_res)
