# -*-coding:utf-8 -*-
# @Time :2019/8/168:39
# @Author : liupengrui
# @FileName :tengxunkaoshi.py

m = int(input())
zhishu = set()
for i in range(3, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:
            zhishu.add(i)
data = set()
for j in zhishu:
    if m - j in zhishu and m - j not in data:
        data.add(j)
print(len(data))


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        le = len(str(x))
        if le == 1:
            return True
        le = le // 2
        x = str(x)
        for i in range(le):
            if x[i] != x[-(i + 1)]:
                return False
        return True


mm = Solution()
print(mm.isPalindrome(1010))

l = '1'
m = '2'
print(l + m)

data = [[] for _ in range(9)]
data[0].append(1)
data[0].append(2)
print(data)
