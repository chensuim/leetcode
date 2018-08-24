#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/2 下午4:49
# @Author : Sui Chen


class minStack(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def push(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                self.value, value = value, self.value
                if self.left is None:
                    self.left = minStack(value)
                else:
                    self.left.push(value)
            else:
                if self.right is None:
                    self.right = minStack(value)
                else:
                    self.right.push(value)

    def pop(self):
        value = self.top()
        if value is None:
            raise IndexError('pop from empty stack!')
        if self.left is not None and self.left.value is not None:
            self.value = self.left.value
            self.left.pop()
        elif self.right is not None and self.right.value is not None:
            self.value = self.right.value
            self.right.pop()
        else:
            self.value = None
        return value

    def remove(self, this):
        self.value = this.value
        if this.right is not None:
            this.value = this.right.value
            this.left = this.right.left
            this.right = this.right.right
        else:
            this.value = None

    def top(self):
        return self.value

a = minStack()
a.push(1)
a.push(2)
a.push(-1)
a.pop()
a.pop()
a.pop()
a.push(-5)
a.push(-5)
a.push(-5)
a.push(-5)
a.push(-5)
a.push(-5)
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()


print a.top()

