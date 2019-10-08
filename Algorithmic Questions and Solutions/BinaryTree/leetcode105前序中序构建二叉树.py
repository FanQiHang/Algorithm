# -*-coding:utf-8 -*-
# @Time :2019/8/68:24
# @Author : liupengrui
# @FileName :buildtree.py

# 根据前序和中序遍历构造二叉树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None


class Solution:
    def buildtree(self, pre, mid):
        if not pre:  # 判断前序序列是否为空
            return None

        root = TreeNode(pre[0])
        print(root.val)

        root_index = mid.index(root.val)  # 找到中序遍历中根节点的索引
        lchild_mid = mid[:root_index]
        rchild_mid = mid[root_index + 1:]

        length = len(lchild_mid)
        lchild_pre = pre[1:length + 1]
        rchild_pre = pre[length + 1:]

        root.left = self.buildtree(lchild_pre, lchild_mid)
        root.right = self.buildtree(rchild_pre, rchild_mid)

        return root


if __name__ == '__main__':
    mm = Solution()
    mm.buildtree([8, 5, 1, 7, 10, 12], [1, 5, 7, 8, 10, 12])
