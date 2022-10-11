# @Time: 2022/10/9 16:31
# @Author: 李树斌
# @File : sum.py
# @Software :PyCharm
def sum(arr):
    if arr == []:
        return 0
    elif len(arr) == 1:
        return arr
    else:
        return arr.pop(0)

arr = [2,4,6,8]

print(sum(arr))