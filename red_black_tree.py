#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/29 下午5:39
# @Author : Sui Chen


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = True

    def change_color(self):
        self.color = not self.color


class Tree(object):
    def __init__(self):
        pass

    def insert(self, num, root):
        if root is None:
            return TreeNode(num)
        else:
            if num > root.val:
                root.right = self.insert(num, root.right)
            elif num < root.val:
                root.left = self.insert(num, root.left)
            else:
                pass
            return root

    def delete(self, num, root):
        if root is None:
            return None
        else:
            if num > root.val:
                root.right = self.delete(num, root.right)
                return root
            elif num < root.val:
                root.left = self.delete(num, root.left)
                return root
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    node = self.delete_largest(root.left)
                    node.left = r


    def insert(self, num):
        if num == self.val:
            return
        if num > self.val:
            if self.right is not None:
                self.right.insert(num)
            else:
                self.right = TreeNode(num)
        else:
            if self.left is not None:
                self.left.insert(num)
            else:
                self.left = TreeNode(num)

    def delete(self, num, parent, is_left=True):
        if num == self.val:
            if self.left is None and self.right is None:
                if parent is not None:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            elif self.left is None:
                if is_left:
                    parent.left = self.right
                else:
                    parent.right = self.right
            elif self.right is None:
                if is_left:
                    parent.left = self.left
                else:
                    parent.right = self.left
            else:


        elif num > self.val:
            if self.right is not None:
                self.right.delete(num, self, is_left=False)
        else:
            if self.left is not None:
                self.left.delete(num, self, is_left=True)

