#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


class KMPStatus(object):
    def __init__(self, word):
        self.word = word
        self.charSet = set(self.word)
        self.back_map = self.get_preffix_suffix_map()

    def status_changer(self, this_status, event):
        status = this_status
        while status >=0:
            # 找到完整字符情况下地下移方法
            if status == len(self.word):
                status = self.back_map[status]
            if event == self.word[status]:
                return status + 1
            elif event in self.charSet:
                status = self.back_map[status]
            else:
                return 0
        return 0

    def get_preffix_suffix_map(self):
        preffix_suffix_map = list()
        preffix_suffix_map.append(-1)
        # length presents the length of the substring, preffix_suffix_map map it to its longest sub_length, which has substring[:length] == substring[-length:]
        for length in range(1, len(self.word) + 1):
            max_length = preffix_suffix_map[length - 1]
            new_char = self.word[length - 1]
            preffix_suffix_map.append(0)
            while max_length >= 0:
                # - 1 means transfer length to index, + 1 means to get next index
                if self.word[max_length - 1 + 1] == new_char:
                    preffix_suffix_map[-1] = max_length + 1
                    break
                else:
                    max_length = preffix_suffix_map[max_length]

        return preffix_suffix_map


class BMmap(object):
    def __init__(self, word):
        self.left_suffix_map = self.create_left_suffix_map(word)
        self.rightest_char_map = self.create_rightest_char_map(word)
        self.length = len(word)
        self.found_move = self.left_suffix_map[len(word)]

    def move(self, bad_char, len_suffix):
        if bad_char is None:
            return self.length - 1 -  self.found_move
        if bad_char in self.rightest_char_map:
            char_pos = self.rightest_char_map[bad_char]
        else:
            char_pos = -1
        suffix_pos = self.left_suffix_map[len_suffix]
        return max(self.length - 1 - suffix_pos, self.length - 1 - len_suffix - char_pos)

    @staticmethod
    def get_common_suffix(str_a, str_b):
        count = 1
        while count <= min(len(str_a), len(str_b)):
            if str_a[-count] != str_b[-count]:
                break
            count += 1
        count -= 1
        return count

    @staticmethod
    def find_max_less(sorted_list, target):
        if not sorted_list or target < sorted_list[0]:
            return -1
        l = 0
        r = len(sorted_list) - 1
        while l < r - 1:
            m = (l + r) / 2
            if sorted_list[m] < target:
                # 防止target 在 [m, m+1)间
                l = m
            elif sorted_list[m] > target:
                r = m
            else:
                return sorted_list[m]
        try:
            if target > sorted_list[l + 1]:
                return sorted_list[l + 1]
        finally:
            return sorted_list[l]

    @staticmethod
    def create_left_suffix_map(word):
        # 不能要-1，因为全长的shared suffix永远是自己
        common_suffix_map = map(lambda x: BMmap.get_common_suffix(word[:x + 1], word), range(len(word) - 1))
        # 仅针对全长都可找到的suffix
        full_length_suffix_map = dict()
        for index, length in enumerate(common_suffix_map):
            full_length_suffix_map[length] = index
        partial_length_suffix = list()
        for index, length in enumerate(common_suffix_map):
            # 头即尾的index
            if length == index + 1:
                partial_length_suffix.append(length)
        left_suffix_map = [len(word) - 1]
        for i in range(len(word) - 1, -1, -1):
            length = len(word) - i
            if length in full_length_suffix_map:
                left_suffix_map.append(full_length_suffix_map[length])
            else:
                left_suffix_map.append(BMmap.find_max_less(partial_length_suffix, length))
        return left_suffix_map

    @staticmethod
    def create_rightest_char_map(word):
        rightest_char_map = dict()
        for index, char in enumerate(word):
            rightest_char_map[char] = index
        return rightest_char_map



def bm_find(text, word):
    if len(text) < len(word):
        return -1
    word_bm_map = BMmap(word)

    def looking_for(word, index):
        bad_char = None
        i = 0
        for i in range(len(word)):
            if word[-i-1] != text[index-i]:
                bad_char = text[index - i]
                break
        return bad_char, i
    index = len(word) - 1
    appeared_indexes = list()
    while index <= len(text) - 1:
        bad_char, len_suffix = looking_for(word, index)
        if bad_char is None:
            appeared_indexes.append(index - (len(word) - 1))
        index += word_bm_map.move(bad_char, len_suffix)
    return appeared_indexes


def kmp_find(text, word):
    if len(text) < len(word):
        return -1
    word_status_machine = KMPStatus(word)
    status = 0
    appeared_indexes = list()
    for index, char in enumerate(text):
        status = word_status_machine.status_changer(status, char)
        if status == len(word):
            # index - length to get the index of the last index just before the found word but we need to return the index of first char of the found word. Thus, + 1 to get it.
            appeared_indexes.append(index - len(word) + 1)

    return appeared_indexes


def force_search(text, word):
    appeared_indexes = list()
    # + 1 to have the first char included
    for i in range(len(text) - len(word) + 1):
        if text[i: i+len(word)] == word:
            appeared_indexes.append(i)
        '''
        to_add = True
        for j in range(len(word)):
            if text[i + j] != word[j]:
                to_add = False
                break
        if to_add:
            appeared_indexes.append(i)
        '''
    return appeared_indexes

with open('bm_search.py', 'r') as f:
    text = f.read()
import time
word = 'create_rightest_char_map' * 500

text *= 100
b = time.time()
bm = bm_find(text, word)
ebm = time.time()
kmp = kmp_find(text, word)
ekmp = time.time()
fs = force_search(text, word)
efs = time.time()
print (ebm - b), (ekmp - ebm), (efs-ekmp)
