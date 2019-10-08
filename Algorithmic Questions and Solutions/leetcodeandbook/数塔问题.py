# -*-coding:utf-8 -*-
# @Time :2019/8/517:14
# @Author : liupengrui
# @FileName :shuta.py

# 动态规划求解数塔问题
import copy

mat = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# mat = [[9], [12, 15], [10, 6, 8], [2, 18, 9, 5], [19, 7, 10, 4, 16]]
ls_data = []
for i in range(len(mat)):
    ls_data.append([1] * (i + 1))
print(ls_data)
# 深拷贝
ls_data = copy.deepcopy(mat)

for i in range(len(mat) - 2, -1, -1):  # 倒数第二行
    for j in range(len(mat[i])):  # 倒数第一行
        mat[i][j] = max(mat[i + 1][j] + mat[i][j], mat[i + 1][j + 1] + mat[i][j])

# 获取路径
ls = [ls_data[0][0]]  # 存储路径的值
k = 0
for i in range(len(mat) - 1):
    for j in range(2):
        res = mat[i][k + j] - ls_data[i][k + j]
        if res == mat[i + 1][k + j]:
            ls.append(ls_data[i + 1][k + j])
            k = k + j
            break

print(mat, ls_data, ls)
