# -*- encoding: utf-8 -*-
"""
@File    : 构建二叉树.py
@Time    : 2019/9/9 22:02
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def listcreattree(root, ls, i):
    if i < len(ls):
        if ls[i] == '#':
            return None
        else:
            root = Node(ls[i])
            root.left = listcreattree(root.left, ls, 2 * i + 1)
            root.right = listcreattree(root.right, ls, 2 * i + 2)
            return root
    return root


# 打印二叉树
def function(root):
    A = []
    result = []
    if not root:
        return result
    A.append(root)  # list A中存储结点
    while A:
        current_root = A.pop(0)
        result.append(current_root.val)
        if current_root.left:
            A.append(current_root.left)
        if current_root.right:
            A.append(current_root.right)
    return result


class Solution:

    def __init__(self):

        self.ans = None

    def lowestCommonAncestor(self, root, p, q):

        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


if __name__ == '__main__':
    ls = ['1', '2', '3', '#', '4', '5']
    root = None
    root = listcreattree(root, ls, 0)
    print(function(root))
    mm = Solution()
    print(mm.lowestCommonAncestor(root, root.left.right, root.left).val)
