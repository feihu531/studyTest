# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 16:36
# @Author  : zhujg
# @File    : fibonacci.py
# @Software: PyCharm

'''
fibnacci功能实现
'''
def fib(n):
    count = 0
    num1 = 0
    num2 = 1
    if isinstance(n, int):
        while count < n:
            res = num1                      #开始时res = num1
            num1, num2 = num2, num1+num2    #实现前两数相加之和是第三个数，并将原来的num2赋给num1，相加后结果的赋给num2
            count += 1
            yield res
    else:
        print('Input arguments Error!')

if __name__ == '__main__':                  #验证输入类型及返回
    # n = int(input("输入需要打印的fib数字："))
    n = input("输入需要打印的fib数字：")
    # print(n.isdigit())
    try:
        if n.isdigit():
            testfib = fib(int(n))           #注意input输入过来的是string，需要将其值转变为int，即fib的参数
            for i in testfib:
                print(i)
        else:
            # fib(n)
            print(fib(n))
    except Exception as e:
        print(e)

