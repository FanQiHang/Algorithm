# -*-coding:utf-8 -*-
# @Time :2019/8/1620:17
# @Author : liupengrui
# @FileName :leetcode38.py

class Solution:
    def countAndSay(self, n: int) -> str:
        data = [[] for _ in range(n)]
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        data[0] = [1]
        data[1] = [1, 1]

        for i in range(2, n):
            print('ii', data)
            x = data[i - 1]
            print('iii', x)
            start = 0
            res = 0
            dict = {}
            flag = False
            for j in range(len(x)):
                if x[start] == x[j]:
                    res += 1
                    if x[start] not in dict:
                        dict[x[start]] = 0
                    dict[x[start]] += 1
                else:
                    start = start + res
                    res = 1
                    flag = True
                if not flag:
                    data[i].append(res)
                    data[i].append(x[start])
                    dict = {}
        return ''.join(data[n - 1])


# mm = Solution()
# print(mm.countAndSay(5))


ls = '12'
num = ls[0]
count = 1
data = []
next = ''
for i in range(1, len(ls)):
    if ls[i] == num:
        count += 1
    else:
        next += str(count) + str(num)
        num = ls[i]
        count = 1
next += str(count) + str(num)
print(next)

s = 'a '
ls = s.strip().split(' ')
print(ls)
x = ls[-1].strip()
print(ls[-1])
print(len(x))


class Solution:
    def plusOne(self, digits):
        data = [1]
        car = 0
        res = []
        while digits:
            if data:
                jiashu = data.pop()
            else:
                jiashu = 0
            temp = digits.pop() + jiashu + car
            print('ii', temp)
            car = temp // 10
            res.append(temp % 10)
            print('ii', res)
        if car:
            res.append(1)
        res.reverse()
        return res


mm = Solution()
print(mm.plusOne([1, 2, 9]))

a = '11'
print(list(map(int, a)))
