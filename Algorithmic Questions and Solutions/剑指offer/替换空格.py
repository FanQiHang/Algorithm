# -*-coding:utf-8 -*-
# @Time :2019/9/610:22
# @Author : liupengrui
# @FileName :替换空格.py


def replaceSpace(s):
    # write code here
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            count = count + 1
    p2 = count * 3 + len(s)
    p1 = len(s)
    ss = ''
    for j in range(len(s) - 1, -1, -1):
        if s[j] != ' ':
            ss = s[j] + ss
            print(ss)
            p1 = p1 - 1
            p2 = p2 - 1
        else:
            if p1 == p2:
                ss = s[j] + ss
                print('ii')
            else:
                ss = '%20' + ss
                p2 = p2 - 3
                p1 = p1 - 1
    print(ss)


replaceSpace('hello world gt')
