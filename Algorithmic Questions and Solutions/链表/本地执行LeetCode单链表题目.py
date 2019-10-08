# -*-coding:utf-8 -*-
# @Time :2019/8/2016:37
# @Author : liupengrui
# @FileName :test03.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkList:
    def __init__(self, node=None):
        self.__head = node

    def is_Empty(self):
        return self.__head is None

    def append(self, item):
        node = ListNode(item)
        if self.is_Empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:  # 查找到尾部的位置
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self.__head
        li = []
        while cur is not None:
            li.append(cur)
            cur = cur.next
        return li

    def find_head(self):
        return self.__head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = head  # 指针
        while True:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
            if p.next is None:
                break
        return head


def print_val(head):
    while head:
        print(head.val)
        head = head.next


ls = SingleLinkList()
data = [1, 1, 2, 3, 3]
for i in data:
    ls.append(i)
print(type(ls))
mm = Solution()
res = mm.deleteDuplicates(ls.find_head())
while res:
    print(res.val, end=' ')
    res = res.next

mm = Solution()
head = ListNode(None)
cur = head
for i in [1, 1, 2, 3, 3]:
    cur.next = ListNode(i)
    cur = cur.next
head = head.next
print(type(head))
res = mm.deleteDuplicates(head)
while res:
    print(res.val, end=' ')
    res = res.next
