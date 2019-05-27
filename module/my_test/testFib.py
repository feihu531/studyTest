# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 16:56
# @Author  : zhujg
# @File    : testFib.py
# @Software: PyCharm
'''
测试my_module中的函数fibonacci
'''
import unittest
from my_module import fibonacci
class TestFibonacciMethods(unittest.TestCase):

    def test_fib_int(self):
        n = int(input('输入测试数据：'))
        res = fibonacci.fib(n)
        for i in res:
            print(i)

    def test_fib_other(self):
        pass

if __name__ == "__main__":
    unittest.main()

