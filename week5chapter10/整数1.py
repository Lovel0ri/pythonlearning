# @Time: 2022/9/20 22:53
# @Author: 李树斌
# @File : 整数1.py
# @Software :PyCharm

#输入二进制整数中查看有多少个数字1，多于四个返回True，否则返回False
def count_1(num):
    count = 0
    while num:
        if num & 1:
            count += 1
        num >>= 1
    return count
print(count_1(10101010))

