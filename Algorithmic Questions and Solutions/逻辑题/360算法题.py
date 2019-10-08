# -*-coding:utf-8 -*-
# @Time :2019/8/99:10
# @Author : liupengrui
# @FileName :test01.py

# 360 编程题 https://blog.csdn.net/flushhip/article/details/79818404


def n1():
    T = int(input())  # 组数
    for i in range(T):
        n = int(input())
        result = 0
        for j in range(n):
            data = input().split(' ')
            x1, y1, x2, y2 = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            result += (x2 - x1 + 1) * (y2 - y1 + 1)
        print(result)


def n2():
    n = int(input())  # 组数
    for i in range(n):
        result = 0
        data = map(int, input().split(' '))
        for j in data:
            result += j
        if result == 0:
            print(-1)
            return
        if result % 5 == 0:  # 这个地方需要注意，如果5个人没有硬币
            print(result // 5)
        else:
            print(-1)


'''
沫璃邀请她的朋友参加周末的派对。沫璃买了3种颜色的气球，现在她要有这些气球来装饰餐桌，每个餐桌只用恰好3个气球装饰，
要求3个气球的颜色不能完全一样，可以是2种或者3种颜色。沫璃想知道这些气球最多能装饰多少张餐桌。
'''


def n3():
    T = int(input())  # 数据数组
    for i in range(T):
        r, g, b = map(int, input().split())  # 三种颜色气球数量
        max_num = int((r + g + b) / 3)  # 最大
        max_color = max([r, g, b])
        flag = max_color - (sum([r, g, b]) - max_color) * 2  # 查看同类颜色多余数量
        if flag > 0:
            max_num = max_num - int(flag / 3)
        print(max_num)


def n4():
    T = int(input())  # 数据数组
    for i in range(T):
        n = int(input())
        m = list(map(int, input().split(' ')))
        m.sort()
        k = len(m) // 2
        if m[k - 1] < m[k]:
            print('YES')
        else:
            print('NO')


def n5():
    n, k = list(map(int, input().split(' ')))
    dp = [[0] * (k + 1) for i in range(n + 1)]
    mod = 772235
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (j * dp[i - 1][j] % mod + (k - (j - 1)) * dp[i - 1][j - 1] % mod) % mod
    print(dp[-1][-1])


if __name__ == '__main__':
    n5()
