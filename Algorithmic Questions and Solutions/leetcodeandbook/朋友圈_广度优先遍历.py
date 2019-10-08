# -*-coding:utf-8 -*-
# @Time :2019/8/1519:51
# @Author : liupengrui
# @FileName :guangduyouxian.py


class Solution:
    def findCircleNum(self, M):

        queen = []
        visited = set()
        ans = 0

        # 实现广度优先遍历
        def bfs(i):
            queen.append(i)
            while queen:
                i = queen[0]
                queen.pop(0)  # 这是一个从右到左的队列
                for j in range(len(M[i])):
                    if M[i][j] and j not in visited:
                        visited.add(j)
                        queen.append(j)

        for i in range(len(M)):
            if i not in visited:
                bfs(i)
                ans += 1
        return ans


mm = Solution()
print(mm.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))

# class Solution:
#     def findCircleNum(self, M):
#         visited, ans = set(), 0
#
#         def dfs(i):
#             for j in range(len(M[i])):
#                 if M[i][j] and j not in visited:
#                     visited.add(j)
#                     dfs(j)
#
#         for i in range(len(M)):
#             if i not in visited:
#                 dfs(i)
#                 ans += 1
#         return ans
