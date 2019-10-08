# -*- encoding: utf-8 -*-
"""
@File    : test02.py
@Time    : 2019/8/5 21:58
@Author  : PerryLiu
@Email   : pengruiliu@163.com
@Software: PyCharm
"""
s = '1-2--3---4-5--6---7'
lr = s[s.find('-') + 1:]
print(lr)

ls = []
if not ls:  # 判断list是空的方法
    print('ii')


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.right:
            return self.minDepth(root.left) + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
