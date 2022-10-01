# @Time: 2022/10/1 14:00
# @Author: 李树斌
# @File : 并行迭代列表.py
# @Software :PyCharm
names = ['anne', 'beth', 'george', 'damon']
ages = [12,45,32,102]
for i in range(len(names)):
    print(names[i],'is',ages[i],'years old')

# zip()函数可以将多个列表，元组或其他序列成对组合成一个元组列表
print(list(zip(names,ages)))
for name, age in zip(names,ages):
    print(name,'is',age,'years old')

print(list(zip(range(5),range(100000))))
