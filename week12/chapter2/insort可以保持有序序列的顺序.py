# @Time: 2022/11/9 16:30
# @Author: 李树斌
# @File : insort可以保持有序序列的顺序.py
# @Software :PyCharm
import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)