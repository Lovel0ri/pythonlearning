# @Time: 2022/10/6 12:40
# @Author: 李树斌
# @File : 6.6.1.py
# @Software :PyCharm
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

print(factorial(5))