# @Time: 2022/9/19 0:54
# @Author: 李树斌
# @File : p171.py
# @Software :PyCharm
#10-1

# with open('10-1.txt') as data:
#     for i in data.readlines():
#         print(i.strip())
#
#     for j in data.read():
#         print(j.strip())
#
#     for k in data.readlines():
#         i = k.strip()
#         list = []
#         list.append(i)
#         print(list)

#10-2
with open('10-1.txt') as data:
    for i in data.readlines():
        print(i.replace('Python','Ruby'))
