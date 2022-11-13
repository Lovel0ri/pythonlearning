# @Time: 2022/11/13 21:10
# @Author: 李树斌
# @File : 对numpy进行行和列的基本操作.py
# @Software :PyCharm
import numpy

a = numpy.arange(12)
# print(a)
# print(a.shape)

# 将a转换为3行4列的矩阵
a.shape = 3, 4
print(a)