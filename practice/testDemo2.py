# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 11:04
# @Author  : zhujg
# @File    : testDemo2.py
# @Software: PyCharm
'''
运行的功能或者测试代码进入__name__下面去写
__name__ = '__main__'
'''
'''
作业：文件打开并copy为另一份文件
'''
# with open('xxx.log', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)
# with open('xxx_copy.txt', 'w', encoding='utf-8') as f:
#     f.write(content)
'''
作业：对文件路径的拼接和是否是文件的判断
'''
# import os
# def file_all(path):
#     list_path = os.listdir(path)            #获取当前目录下的文件及文件夹
#     for i in list_path:
#         full_path = os.path.join(path,i)    #绝对路径和文件拼接
#         if os.path.isdir(full_path):        #判断是否是目录
#             file_all(full_path)
#         else:
#             print (full_path)
#
# file_all(r'E:\PycharmPro\demo')
'''
作业：异常判断
'''
# try:
#     with open('xxx.log', 'r+', encoding='utf-8') as f:
#         f.write('给只读文件中添加文字')
# except NameError as e:
#     print(e)
# except IOError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print('内容写入成功')
#     f.close()

'''
课程：模块和包
'''


