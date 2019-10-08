# -*-coding:utf-8 -*-
# @Time :2019/8/1315:54
# @Author : liupengrui
# @FileName :test03.py


# 实现字符串相乘和相加
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        res = []
        for loc in range(len(num2)):  # multiply
            x2 = ord(num2[len(num2) - 1 - loc]) - ord('0')
            ans, tmp, car = [], 0, 0
            for n1 in num1[::-1]:
                x1 = ord(n1) - ord('0')
                tmp = x1 * x2 + car
                car = tmp // 10
                ans.append(str(tmp % 10))
            if car: ans.append(str(car))
            ans.reverse()
            # 将计算后的结果补位使个位对齐
            ans.extend(['0' for _ in range(loc)])

            i, j, car = len(res) - 1, len(ans) - 1, 0
            res_tmp = []
            while i >= 0 or j >= 0:  # add i=2,j=3
                a1 = ord(res[i]) - ord('0') if i >= 0 else 0
                a2 = ord(ans[j]) - ord('0') if j >= 0 else 0
                tmp = a1 + a2 + car
                car = tmp // 10
                res_tmp.append(str(tmp % 10))
                i, j = i - 1, j - 1
            if car: res_tmp.append('1')
            res_tmp.reverse()
            res = res_tmp
        return ''.join(res)


# m = Solution()
# print(m.multiply('123', '456'))

s1 = '456'
s2 = '1234'
ls1 = [ord(i) - ord('0') for i in s1]
ls2 = [ord(i) - ord('0') for i in s2]
i, j, car = len(ls1) - 1, len(ls2) - 1, 0
res = []
while i >= 0 or j >= 0:
    # 以下两行代码很关键，需要深刻体会
    a1 = ls1[i] if i >= 0 else 0
    a2 = ls2[j] if j >= 0 else 0
    x = a1 + a2 + car
    ans = x % 10
    res.append(str(ans))  # 这里正向加入，最后需要翻转
    car = x // 10
    i, j = i - 1, j - 1
if car:
    res.append('1')
print(res)
res.reverse()
print(''.join(res))
