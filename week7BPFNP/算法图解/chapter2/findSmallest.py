# @Time: 2022/10/8 23:10
# @Author: 李树斌
# @File : findSmallest.py
# @Software :PyCharm

def findSmallest(arr):
    """Find the smallest item in an array"""
    smallest = arr[0]#存储最小值
    smallest_index = 0#存储最小元素的索引
    for i in range(1, len(arr)):#遍历数组
        if arr[i] < smallest:
            smallest = arr[i]#更新最小值
            smallest_index = i#更新最小元素的索引
    return smallest_index

def selectionSort(arr):#对数组进行排序
    """Sort array"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)#找出数组中最小的元素，并将其加入到新数组中
        newArr.append(arr.pop(smallest))
    return newArr
array = [5, 3, 6, 2, 10]

print(array[0])
print(array[1])
print(array[2])
print("")
print(findSmallest(array))
print(selectionSort(array))


"""
存储多个元素时，可使用数组或链表
数组：存储在连续的内存中，可通过索引访问元素，但是插入或删除元素时，需要移动大量元素，效率低
链表：存储在不连续的内存中，插入或删除元素时，只需要修改指针，效率高
"""

"""选择排序
1.找出数组中最小的元素
2.将该元素和数组的第一个元素交换位置
3.在剩下的元素中找出最小的元素，将该元素和数组的第二个元素交换位置
4.重复步骤3，直到将整个数组排序
"""