# @Time: 2022/11/20 16:27
# @Author: 李树斌
# @File : 集合.py
# @Software :PyCharm
haystack = {'111','222','333'}
needles = {'111'}

found = len(needles & haystack)
print(found)