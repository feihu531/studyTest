# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:16
# @Author  : zhujg
# @File    : testIterate.py
# @Software: PyCharm

'''
迭代器
迭代：通过for循环遍历可迭代对象的每一个元素。
可迭代对象：被for循环遍历序列类型，有__iter__方法
迭代器：实现__iter__和__next__方法，一次取一个，只往前，不可往后退
'''
li = [1,2,3,4,5,6]
# print(iter(li))
# print(next(iter(li)))
# it = iter(li)
# print(next(it))
# print(next(it))
# print(li.__iter__())
# print(li.__iter__().__next__())

'''
用while循环取值，步骤：
1.变为迭代器
2.对迭代器进行取值
'''
# li = [1,2,3,4,5,6]
# it = li.__iter__()
# while True:
#     try:
#         b = next(it)
#         print(b)
#     except StopIteration:
#         break
'''
生成器：就是一个函数，也是一个迭代器。通过yield关键字返回多次值，可以保持函数挂起/保存运行状态
迭代器：是一个对象
'''
def fun():
    print('账户名')
    yield 1
    print('密码')
    yield 2
    yield 'other'

if __name__ == '__main__':
    res = fun()
    print(res)
    print(next(res))
    print(next(res))
'''
代码块--》函数--》类--》模块--》包
'''
