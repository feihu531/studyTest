# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 16:45
# @Author  : zhujg
# @File    : testCal.py
# @Software: PyCharm
'''
import:
1.执行调用的函数
2.引入变量名calculate
逻辑函数
'''
# import calculate
# print(calculate.add(5,3))
# from calculate import *       #不推荐这样使用
# from calculate import add, sub
# print(add(3, 5))
# print(sub(4, 6))
# sys.path放的执行文件所在的路径
# from my_module import calculate
# print(calculate.add(1, 2))

'''
包：
1.防止文件名重复
2.加快速度
'''

'''
常用模块random
生成四位的验证码
'''
# import random
# def make_code():
#     res=''
#     for i in range(4):
#         num = random.randint(0, 9)
#         alf1 = chr(random.randint(65, 90))
#         alf2 = chr(random.randint(97, 122))
#         s = str(random.choice([num, alf1, alf2]))
#         res += s
#     return res
# if __name__ == '__main__':
#     print(make_code())

'''
路径的引用，OS模块
'''
# import sys,os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #文件名对应的绝对路径的名称
# sys.path.append(BASE_DIR)
# from my_module import calculate
#
# def logger():
#     pass
# if __name__ == '__main__':
#     print(__file__)
#     calculate.add(2,3)