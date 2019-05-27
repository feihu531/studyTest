# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 13:43
# @Author  : zhujg
# @File    : bubbleSort.py
# @Software: PyCharm

"""bubble sort冒泡排序算法实现"""


def bubble_sort(arr):
    # 第一次for循环遍历次数
    for i in range(len(arr) - 1):
        # 第二次for循环遍历第i轮后剩余次数
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


li = [11, 23, 2, 3, 454, 65, 33, 2, 4, 55]
print(bubble_sort(li))
