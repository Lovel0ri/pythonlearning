# @Time: 2022/9/6 23:16
# @Author: 李树斌
# @File : 7.3.2删除为特定值的所有列表元素.py
# @Software :PyCharm
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)