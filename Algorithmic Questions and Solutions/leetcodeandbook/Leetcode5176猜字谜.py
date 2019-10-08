# -*-coding:utf-8 -*-
# @Time :2019/9/216:45
# @Author : liupengrui
# @FileName :code1.py

ls = [1, 2, 3]
print([*map(str, ls)])
print(list(map(str, ls)))

# 实质是一个匹配问题
import collections

words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]

d = collections.Counter(''.join(sorted(set(w))) for w in words if len(set(w)) <= 7)
print(d)


def f(p):
    cbt = [p[0]]  # 谜面首元素必须放进组合
    for c in p[1:]:  # 谜面首元素其他元素放进组合排好序，以匹配处理后的谜底
        # print('ii', [''.join(sorted(s + c)) for s in cbt])
        cbt += [''.join(sorted(s + c)) for s in cbt]
    print('iii', cbt)
    # 以上代码找到所有可能的组合
    return sum(d[s] for s in cbt if s in d)  # 如果谜面可以匹配谜底，就加上这种类型的谜底的数量


print(list(map(f, puzzles)))  # 利用map实现循环
