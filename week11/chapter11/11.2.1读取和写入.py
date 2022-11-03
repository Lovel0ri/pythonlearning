# @Time: 2022/11/2 0:24
# @Author: 李树斌
# @File : 11.2.1读取和写入.py
# @Software :PyCharm
# f = open('somefile.txt', 'w')
# f.write('Hello, world!')
# f.close()

f = open('somefile.txt', 'r')

print(f.read(3))
f.close()