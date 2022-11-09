# @Time: 2022/11/9 13:14
# @Author: 李树斌
# @File : 切片.py
# @Software :PyCharm
list1 = list(range(10))
list1[2:5] = [20,30]
print(list1)

del list1[5:7]
print(list1)

list1[3::2] = [11,22]
print(list1)