#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/6 下午5:23
# @Author : Sui Chen
import sys


class TreeNode(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None



def construct_from_list(a_list):
    if not a_list:
        return
    root = TreeNode(a_list[0])
    this_layer = [root]
    i = 1
    while i < len(a_list):
        next_layer = list()
        for tree_root in this_layer:
            try:
                if a_list[i] is not None:
                    tree_node = TreeNode(a_list[i])
                    tree_root.left = tree_node
                    next_layer.append(tree_node)
                if a_list[i+1] is not None:
                    tree_node = TreeNode(a_list[i + 1])
                    tree_root.right = tree_node
                    next_layer.append(tree_node)
                i += 2
                this_layer = next_layer
            except IndexError:
                i += 2
                break
    return root


class Solution(object):
    left_dict = dict()
    right_dict = dict()

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -sys.maxint
        return max(self.maxLeft(root), self.maxRight(root), self.maxRight(root) + self.maxLeft(root) - root.val,
                   self.maxPathSum(root.left), self.maxPathSum(root.right))

    def maxLeft(self, root):
        if root is None:
            return -sys.maxint
        if root in self.left_dict:
            return self.left_dict[root]
        result = max(root.val, root.val + self.maxLeft(root.left), root.val + self.maxRight(root.left))
        self.left_dict[root] = result
        return result

    def maxRight(self, root):
        if root is None:
            return -sys.maxint
        if root in self.right_dict:
            return self.right_dict[root]
        result = max(root.val, root.val + self.maxLeft(root.right), root.val + self.maxRight(root.right))
        self.right_dict[root] = result
        return result




