# @Time: 2022/9/3 14:30
# @Author: 李树斌
# @File : p145练习使用列表.py
# @Software :PyCharm

#sort原地排序
data = [6,3,1,2,4,5]
data.sort()
print(data)

#复制排序
data = [6,3,1,2,4,5]
data2= sorted(data)
print(data2)
print(data)