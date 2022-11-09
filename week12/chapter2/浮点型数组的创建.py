# @Time: 2022/11/9 17:18
# @Author: 李树斌
# @File : 浮点型数组的创建.py
# @Software :PyCharm


from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
#name = array("d", ["nihao"])#TypeError: must be real number, not str
#print(name)
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)