# @Time: 2022/10/1 14:13
# @Author: 李树斌
# @File : 迭代时获取索引.py
# @Software :PyCharm
names = ['anne', 'beth', 'george', 'damon']
for index, name in enumerate(names):
    print(index,name)

# enumerate()函数可以将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中

# enumerate()函数可以接收两个参数，第一个为序列，第二个为下标起始位置

list = [4,3,6,8,3]
print(id(sorted(list)))

list.append(9)
print(id(list))