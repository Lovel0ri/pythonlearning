# @Time: 2022/11/2 0:39
# @Author: 李树斌
# @File : 使用fileinput迭代行.py
# @Software :PyCharm
import fileinput

# for line in fileinput.input('somefile.txt'):
#     print(line, end='')

with open('somefile.txt', 'r') as f:
    for line in f:
        print(line, end='')