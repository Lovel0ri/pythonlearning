# @Time: 2022/9/19 0:54
# @Author: 李树斌
# @File : p171.py
# @Software :PyCharm
#10-1

with open('10-1.txt') as data:
    # for i in data.readlines():
    #     print(i.strip())
    # for i in data.read():
    #     print(i.strip())
    for i in data.readlines():
        i = i.strip()
        my_i = [i]

print(my_i)
