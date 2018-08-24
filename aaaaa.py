import copy


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree import construct_from_list


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        root.p = None
        stack = [root]
        while stack:
            parent = stack.pop()
            if parent.left:
                parent.left.p = parent
                stack.append(parent.left)
            if parent.right:
                parent.right.p = parent
                stack.append(parent.right)
        pp = []
        while p:
            pp.append(p)
            p = p.p
        qp = []
        while q:
            qp.append(q)
            q = q.p
        for i in xrange(min(len(pp), len(qp))):
            if pp[~i] != qp[~i]:
                return pp[~i+1]



func = None
for attr in Solution.__dict__:
    if callable(Solution.__dict__[attr]) and not attr.startswith('__'):
        func = Solution.__dict__[attr]


args = [
    construct_from_list([3,5,1,6,2,0,8,None,None,7,4]),
    5,
    1
]

print func(Solution(), *args)







