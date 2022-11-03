# @Time: 2022/11/2 0:28
# @Author: 李树斌
# @File : 随机存取.py
# @Software :PyCharm

f = open(r'somefile.txt', 'w')
f.write('01234567890123456789')
print(f.seek(5))
f.write('hello,world')
f = open(r'somefile.txt', 'r')
print(f.read())
f.close()

f = open(r'somefile.txt', 'r')
print(f.read(3))
print(f.read(2))
print(f.tell())