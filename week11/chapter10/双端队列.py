# @Time: 2022/11/1 22:47
# @Author: 李树斌
# @File : 双端队列.py
# @Software :PyCharm
from collections import deque
q = deque(range(5))
print(q)
q.append(5)
print(q)
q.appendleft(6)
print(q)
#rotate() 方法用于旋转deque中的元素，如果n为正，则向右旋转，如果n为负，则向左旋转。
q.rotate(3)
print(q)
q.rotate(5)
print(q)
q.rotate(3)
print(q)