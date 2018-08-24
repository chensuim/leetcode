#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/12 下午6:14
# @Author : Sui Chen

class PrimeGenerator(object):
    def __init__(self):
        self.prime_list = [2]

    def get_next_prime(self):
        num = self.prime_list[-1] + 1
        while True:
            if self._is_prime(num):
                self.prime_list.append(num)
                return num
            else:
                num += 1

    def _is_prime(self, num):
        for i in self.prime_list:
            if i * i > num:
                return True
            if num % i == 0:
                return False


prime_generator = PrimeGenerator()
for i in range(26):
    prime_generator.get_next_prime()
print prime_generator.prime_list
