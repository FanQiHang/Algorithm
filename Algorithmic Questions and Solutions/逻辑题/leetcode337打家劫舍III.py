# -*-coding:utf-8 -*-
# @Time :2019/7/2216:20
# @Author : liupengrui
# @FileName :train337.py


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return max(self.func(root))
        return 0

    def func(self, root):
        lv = rv = (0, 0)
        if root.left:
            lv = self.func(root.left)
        if root.right:
            rv = self.func(root.right)
        return root.val + lv[1] + rv[1], max(lv) + max(rv)
