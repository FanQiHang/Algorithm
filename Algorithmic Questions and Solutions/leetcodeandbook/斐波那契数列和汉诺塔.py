# -*-coding:utf-8 -*-
# @Time :2019/7/249:42
# @Author : liupengrui
# @FileName :tset01.py

# 斐波那契数列和汉诺塔的实现


# 斐波那契数列,第n个数是多少
def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)


# 汉诺塔问题

def hano(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hano(n - 1, x, z, y)  # 将n-1个借助z移动到y
        print(x, '-->', z)  # 将最后一个移动到z
        hano(n - 1, y, x, z)  # 将n-1个借助x移动到z


print(f(4))
