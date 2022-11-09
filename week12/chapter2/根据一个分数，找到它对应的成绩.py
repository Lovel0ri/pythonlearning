# @Time: 2022/11/9 15:49
# @Author: 李树斌
# @File : 根据一个分数，找到它对应的成绩.py
# @Software :PyCharm

"""def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo"""

import bisect
def grade(score,breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    print(i)
    return grades[i]

print(grade(91))
#print([grade(score) for score in [33,99,77,70,89,90,100]])