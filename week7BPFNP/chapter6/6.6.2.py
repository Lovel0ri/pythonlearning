# @Time: 2022/10/6 12:48
# @Author: 李树斌
# @File : 6.6.2.py
# @Software :PyCharm
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
print(power(5,2))

#5 * power(5,1) * power(5,0) = 5*5*1 = 25