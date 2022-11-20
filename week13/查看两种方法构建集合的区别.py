# @Time: 2022/11/20 16:33
# @Author: 李树斌
# @File : 查看两种方法构建集合的区别.py
# @Software :PyCharm
from dis import dis

print(dis('{1}'))

print(dis('set([1])'))