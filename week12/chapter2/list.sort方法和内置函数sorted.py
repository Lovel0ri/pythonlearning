# @Time: 2022/11/9 15:12
# @Author: 李树斌
# @File : list.sort方法和内置函数sorted.py
# @Software :PyCharm

list1 = [2,4,1,5,7,3,6,8,9]
print(id(list1))
list1.sort()
print(list1)
print(id(list1))

list1 = [2,4,1,5,7,3,6,8,9]
print(id(list1))
# sorted()函数返回一个新的列表，而不是在原来的基础上进行排序
list2 = sorted(list1)
print(list2)
print(id(list2))
