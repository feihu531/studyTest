# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 13:57
# @Author  : zhujg
# @File    : selectionSort.py
# @Software: PyCharm

"""选择排序"""


def selection_sort(arr):
    # 循环次数
    for i in range(len(arr) - 1):
        # 开始元素设为最小元素（小标表示）
        min_index = i
        # 最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 若当前元素比最小元素小，把当前元素的下标给最小元素下标
                min_index = j
        # 循环一轮后将最小元素和起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


li = [22, 333, 1, 2, 3, 44, 555, 6, 5, 444]
print(selection_sort(li))
