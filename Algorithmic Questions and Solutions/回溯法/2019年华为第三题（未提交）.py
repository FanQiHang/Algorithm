# -*-coding:utf-8 -*-
# @Time :2019/8/158:48
# @Author : liupengrui
# @FileName :huawei3.py

import numpy as np


def dfsTravse(m, start, n, grapha):  # m为图的长度，i为起始点，n为深度
    list_friend = {}
    visited = []
    ls = [0]  # 存储中间结果
    _ls = [start]
    for k in range(m):
        visited.append(False)

    visited[start] = True  # 将开始结点的位置设置为True

    recommend = 0
    index = n

    dfs(m, start, n, grapha, recommend, visited, list_friend, ls, _ls, index)

    # 对list_friend进行判断
    # for i in range(m):
    #     if grapha[start][i] != 0 and i in list_friend:
    #         list_friend.pop(i)

    return list_friend


def dfs(m, start, n, grapha, recommend, visited, list_friend, ls, _ls, index):
    # 将结果返回
    if n == 0:
        list_friend[start] = recommend  # start为最终的结点值
        return

    for j in range(m):

        if not grapha[start][j] == 0 and not visited[j]:
            recommend += grapha[start][j]
            ls.append(recommend)
            _ls.append(j)
            visited[j] = True

            dfs(m, j, n - 1, grapha, recommend, visited, list_friend, ls, _ls, index)  # j为i的下一个节点

            visited[j] = False
            ls.pop()
            recommend = ls[-1]
            # recommend = grapha[start][j]  # 推荐度应该重置，但是不应该是0，应该为上一个状态的值

    for ii in range(m):
        if grapha[_ls[index - 2]][ii] != 0 and ii in list_friend:  # 删除5-3-8和5-8-3的值,index表示度
            list_friend.pop(ii)


if __name__ == '__main__':
    T = int(input("T"))
    for t in range(T):
        line1 = input()
        m, start, n = int(line1.split(" ")[0]), int(line1.split(" ")[1]), int(line1.split(" ")[2])
        line2 = input()
        list2 = line2.split(" ")
        k = int(list2[0])
        grapha = np.zeros((m, m))
        for v in range(1, len(list2), 3):
            i = int(list2[v])
            j = int(list2[v + 1])
            w = int(list2[v + 2])
            grapha[j][i] = w  # 填充矩阵出现问题，填充之后是一个上三角形矩阵，需要补充这一行代码
            grapha[i][j] = w
        print(grapha)
        print(dfsTravse(m, start, n, grapha))

# [[0. 0. 0. 5. 9. 0. 8. 5. 0. 0.]
#  [0. 0. 6. 0. 0. 0. 3. 0. 0. 0.]
#  [0. 6. 0. 0. 0. 0. 0. 0. 0. 7.]
#  [5. 0. 0. 0. 3. 3. 0. 0. 3. 3.]
#  [9. 0. 0. 3. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 3. 0. 0. 0. 0. 9. 0.]
#  [8. 3. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [5. 0. 0. 0. 0. 0. 0. 0. 9. 0.]
#  [0. 0. 0. 3. 0. 9. 0. 9. 0. 0.]
#  [0. 0. 7. 3. 0. 0. 0. 0. 0. 0.]]


# 2
# 10 5 2
# 13 0 3 5 0 4 9 0 6 8 0 7 5 1 2 6 1 6 3 2 9 7 3 4 3 3 5 3 3 8 3 3 9 3 5 8 9 7 8 9
# 10 0 2
# 13 0 3 5 0 4 9 0 6 8 0 7 5 1 2 6 1 6 3 2 9 7 3 4 3 3 5 3 3 8 3 3 9 3 5 8 9 7 8 9

# 7 0 4 9
# 1 5 8 9
