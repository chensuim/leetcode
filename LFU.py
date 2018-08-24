#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/24 下午12:15
# @Author : Sui Chen


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.before = None

    def __str__(self):
        result = str()
        head = self
        while head:
            result += str(head.val) + ' -> '
            head = head.next
        return result

    def reverse(self):
        result = str()
        head = self
        while head:
            result += str(head.val) + ' -> '
            head = head.before
        return result


class LinkedHashSet(object):
    def __init__(self):
        self.node_dict = dict()
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.before = self.head
        self.length = 0

    def add(self, key):
        node = ListNode(key)
        self.head.next.before, self.head.next, node.before, node.next = node, node, self.head, self.head.next
        self.node_dict[key] = node
        self.length += 1

    def remove(self, key):
        node = self.node_dict[key]
        node.before.next, node.next.before = node.next, node.before
        del self.node_dict[key]
        self.length -= 1

    def pop(self):
        last_node = self.tail.before
        self.remove(last_node.val)
        return last_node.val

    def __len__(self):
        return self.length


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.frequency = dict()
        self.val = dict()
        self.frequency_set = dict()
        self.min = 1
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.val:
            self.update(key)
            return self.val[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if len(self.val) >= self.capacity and key not in self.val:
            self.pop()
        if key in self.val:
            self.val[key] = value
            self.update(key)
        else:
            self.val[key] = value
            self.frequency[key] = 0
            self.update(key)
            self.min = 1

    def pop(self):
        frequency_set = self.frequency_set[self.min]
        key = frequency_set.pop()
        del self.val[key]
        del self.frequency[key]
        if len(self.frequency_set) == 0:
            self.min += 1

    def update(self, key):
        frequency = self.frequency[key]
        self.frequency[key] += 1
        if frequency in self.frequency_set:
            frequency_set = self.frequency_set[frequency]
            frequency_set.remove(key)
            if len(frequency_set) == 0 and frequency == self.min:
                self.min += 1
        up_frequency = frequency + 1
        if up_frequency in self.frequency_set:
            up_frequency_set = self.frequency_set[up_frequency]
            up_frequency_set.add(key)
        else:
            up_frequency_set = self.frequency_set[up_frequency] = LinkedHashSet()
            up_frequency_set.add(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

action = ["put","put","get","get","get","put","put","get","get","get","get"]
param = [[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
a = LFUCache(3)
for index in range(len(action)):
    if action[index] == 'put':
        a.put(param[index][0], param[index][1])
        print None
    else:
        print a.get(param[index][0])