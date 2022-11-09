# @Time: 2022/11/9 14:07
# @Author: 李树斌
# @File : 序列的增量赋值.py
# @Software :PyCharm
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [4,5,6]
list1.append(list2)
print(list1)

list1 = [1,2,3]
list1.extend(list3)
print(list1)

