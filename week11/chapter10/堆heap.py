# @Time: 2022/11/1 22:17
# @Author: 李树斌
# @File : 堆heap.py
# @Software :PyCharm
from heapq import *
from random import shuffle
data = list(range(10))
print(data)
#shuffle() 方法将序列的所有元素随机排序。
shuffle(data)
heap = []
heap2 = []
for n in data:
    heappush(heap2, n)
print(heap)
print(heap2)
print(heappop(heap2))
