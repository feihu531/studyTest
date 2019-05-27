# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 10:31
# @Author  : zhujg
# @File    : testDemo1.py
# @Software: PyCharm

# def foo():
#     name = 'lihaifeng'
#     def bar():
#         name = 'wpq'
#         def tt():
#             print(name)
#         return tt
#     return bar

# foo()()()
# r1 = foo()
# print(r1,r1())
# r2 = r1()
# print(r2,r2())

# lambda x:x+1
# def calc(x):
#     return x+1
#
# print(calc(10))

# func = lambda x:x+1
# print(func(10))

# lambda和其他函数一起使用，不建议独立存在的使用
# func = lambda name:name+'_sb'
# print(func('alex'))

# def change_name(name):
#     return name + '_sb'
#
# print(change_name('alex'))

# 高阶函数：1.把函数接收的参数是一个函数名；2.返回值包含函数
# 返回值可以是任意函数
# def bar():
#     print("from bar")
# def foo():
#     print('from foo')
#     return bar
# n = foo()
# n()
# foo()
# print(foo())
# 尾递归，函数的最后一步（并非最后一行）调用另一个函数，递归效率低

# res = []
# num_1 = [1,2,3,4,23,22,7]
# for i in num_1:
#     res.append(i**2)
#
# print(res)

# num = [1,2,3,4,2,2,7]
# def map_test(array):
#     res = []
#     for i in num:
#         res.append(i**2)
#     return res
# ret = map_test(num)
# print(ret)

# num = [1,2,3,4,2,2,7]
# def map_test(func,arr):
#     ret = []
#     for i in arr:
#         res = func(i) #add_one(i)
#         ret.append(res)
#     return ret
# print(map_test(lambda x:x+1,num))

# num = [1,2,3,4,2,2,7]
# aa = map(lambda x:x+1,num)
# print(list(aa))

# msg = "adfnjdngalfl"
# print(list(map(lambda x:x.upper(),msg)))

# reduce 合并或压缩成一个序列；map 按照原有序列处理序列中每个元素值；filter序列中所有制筛选一遍有生成一个序列
# map()函数处理序列中的每个元素，得到的结果是一个序列，该序列元素个数及位置与原来一样
# filter()函数遍历序列中的每个元素，判断每个元素得到一个bool值，如果是True,则留下来
# reduce()函数处理序列，把序列进行合并操作
# from functools import reduce
# li = [1,2,3,4,5,6]
# # reduce(func,li,init)  #init 表示初始操作值
# res = reduce(lambda x,y:x+y,li,2)
# res1 = reduce(lambda x,y:x+y,li)
# print(res,res1)

# name = ['alex_sb','linhaifeng']
# res = filter(lambda x:not x.endswith('sb'),name)
# print(list(res))

# 空，None，0的布尔值返回未False
# print(all([1, 2, 'None', '']))
# print(all(['']))
# print(bin(2))
# print(bool())
# name = '你好'
# print(bytes(name,encoding='utf-8'))
# print(bytes('你好',encoding='utf-8').decode())
# print(bytes(name,encoding='gbk').decode('gbk'))
# print(bytes(name,encoding='ascii'))#ascii码不能encode中文
# eval()：1.字符串中的数据结构提取出来；2.把字符传中的数学运算做一遍
# print(bin(10))
# print(hex(10))
# print(oct(12 ))

# f = open('test1.txt','rb',encoding='utf-8') #b的放肆不能指定编码
# f = open('test1.txt','r',encoding='utf-8')
# f = open('test1.txt','rb')
# data = f.read()
# # '字符串'-------encode------>bytes  叫--->编码
# # bytes-------decode------>'字符串'  叫--->解码
# # 二进制处理文件的一种方式，可以实现不同文件类型及跨平台操作
# print(data)
# print(data.decode('utf-8'))

# f = open('test2.py', 'wb')
# f.write(bytes('11111\n', encoding='utf-8'))
# f.write(bytes('测试', encoding='utf-8'))

# f = open('test2.py', 'ab')
# f.write(bytes('\n哈哈', encoding='utf-8'))

# f = open('a.txt', 'r', encoding='utf-8', newline='') #读取文件中真正的换行符
# data = f.readlines()
# print(data)
# print(f.tell())
# f.seek(3)       #光标移动所处位置，移动几个字节，seek打开建议以rb模式打开
# print(f.tell()) #告诉光标当前的位置
# print(f.read())
# print(f.read(1))   #读取字符数
# f = open('a.txt', 'r+', encoding='utf-8', newline='')
# f.truncate(10) #文件截取，open函数模式需要有w权限，但是不能有w+

# 循环文件推荐的方式
# 获取日志文件最后一行
# file.seek()方法标准格式是：file.seek(offset,whence)
# offset：开始的偏移量，也就是代表需要移动偏移的字节数
# whence：给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。whence值为空没设置时会默认为0。
# f = open('xxx.log','rb')
# for i in f:
#     offs = -10
#     while True:
#         f.seek(offs,2)
#         data = f.readlines()
#         if len(data) > 1:
#             print('文件最后一行是：%s' %(data[-1].decode('utf-8')))
#             break
#         offs = offs*2
# f.close()


# f = open('xxx.log', 'r', encoding='utf-8')
# print(f.name)
# data = f.read()
# print(data)
# data_line = f.readline()
# print(data_line)
# data_lines = f.readlines()
# print(data_lines)
# f.close()

# 获取文件的某一行或者从第n行到第m行，输出一个list
# import linecache
# data_2 = linecache.getlines('xxx.log')[0:3]
# print(data_2)

# 一、迭代器和生成器
# 1.迭代器：__iter__();__next__()
# for循环迭代
# li = [1,2,3,4]
# for i in li:
#     print(i)

# while循环迭代
# li = [1,2,3,4,5,6]
# index = 0
# while index < len(li):
#     print(li[index])
#     index += 1

# next()方法实际上是--->iter.__next__()，直到StopIteration结束，for已经处理了StopIteration错误提示
# li = [1,2,3]
# iter = li.__iter__()
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())

# 2.生成器：yield
# 生成器执行一次next才能取一次值
# 生成器只能遍历一次
# 列表解析,三元运算符
# li = ['鸡蛋%s' %i for i in range(10) if i>5]
# print(li)

# def test():
#     for i in range(4):
#         yield i
#         # print(i)
#
# t = test()
# t1 = (i for i in t)
# t2 = (i for i in t1)
# print(list(t1))
# print(list(t2))

# 3.装饰器
'''
装饰器他人的器具，本身可以是任意可调用对象，被装饰者也可以是任意可调用对象。
强调装饰器的原则：1 不修改被装饰对象的源代码 2 不修改被装饰对象的调用方式
装饰器的目标：在遵循1和2的前提下，为被装饰对象添加上新功能
*****装饰器=高阶函数+函数嵌套+闭包
'''
# 引例：
# import time
# def cal(l):
#     start_time = time.time()
#     res = 0
#     for i in l:
#         time.sleep(0.001)
#         res += i
#     stop_time = time.time()
#     print("函数运行时间 %s" %(stop_time - start_time))
#     return res
# print(cal(range(100)))
# def cal(l):
#     # start_time = time.time()
#     res = 0
#     for i in l:
#         # time.sleep(0.001)
#         res += i
#     # stop_time = time.time()
#     # print("函数运行时间 %s" %(stop_time - start_time))
#     return res
# r = cal(range(20))
# print(r)

'''
高阶函数的定义：
1.函数接收的参数是一个函数名
2.函数的返回值是一个函数名
3.满足上述任意一个，都可以称为高阶函数
'''
# import time
# def foo():
#     time.sleep(0.001)
#     print('一千年以后')
#
# def test(func):
#     # print(func)
#     start_time = time.time()
#     func()#运行函数的统计时间，也就是foo()
#     stop_time = time.time()
#     print("函数运行时间是：%s" %(stop_time-start_time))
# # foo() #这个是正常调用foo函数的方式
# test(foo)

# def foo():
#     print('from foo')
# def test(func):
#     return func
# # res = test(foo)
# foo = test(foo)
# foo()
'''
实现了高阶函数，但是没有实现新增功能，即多执行了一次foo()
# '''
# import time
# def foo():
#     time.sleep(0.002)
#     print('来自 foo')
# def timer(func):
#     start_time = time.time()
#     func()#运行函数的统计时间，也就是foo()
#     stop_time = time.time()
#     print("函数运行时间是：%s" %(stop_time-start_time))
#     return func #多运行了一步
# foo = timer(foo)
# foo()
'''
函数嵌套：在函数里面再定义了一个函数
*函数递归：函数里面调用自己
'''
# def father(name):
#     # print('from father %s'%name)
#     def son():
#         print('我的father是 %s'%name)
#         def gandson():
#             print('我的爷爷是 %s'%name)
#         gandson()
#     # print(locals())#打印当前层的局部变量,函数即变量，也就是也包含函数名
#     son()
# father('alex')
'''
闭包：相当于函数作用域
'''
'''
装饰器
'''
# import time
# # 装饰器的架子
# def timer(func):    #func = test  传入函数名作为参数
#     def wrapper():
#         start_time = time.time()
#         func()  #相当于运行test()
#         stop_time = time.time()
#         print('运行时间是 %s' %(stop_time-start_time))  #新增统计时间功能
#     return wrapper  #返回函数名
#
# def test():
#     time.sleep(0.005)
#     print('test函数运行完毕')
#
# # test()
# test = timer(test) #返回wrapper的地址  ，和上面test()调用相比，多做了一次赋值
# test()              #执行的wrapper()
# # @timer 相当于test = timer(test)


import time
# 装饰器的架子
def timer(func):    #func = test  传入函数名作为参数
    def wrapper():
        start_time = time.time()
        func()  #相当于运行test()
        stop_time = time.time()
        print('%s函数的运行时间是 %s' %(func,stop_time-start_time))  #新增统计时间功能
    return wrapper  #返回函数名
@timer      # @timer 相当于test = timer(test)
def test():
    time.sleep(0.005)
    print('test函数运行完毕')

# test()
# test = timer(test)  #返回wrapper的地址，和上面test()调用相比，多做了一次赋值
# test()              #执行的wrapper()
@timer
def test_instance():
    for i in range(10000):
        isinstance(888,int)
@timer
def test_type():
    for i in range(10000):
        type(888)

test_instance()
test_type()
