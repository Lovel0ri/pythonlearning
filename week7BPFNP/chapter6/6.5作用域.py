# @Time: 2022/10/5 19:38
# @Author: 李树斌
# @File : 6.5作用域.py
# @Software :PyCharm
# def foo():
#     x = 10
#     return x

x = 1
def change_global():
    global x
    x = x + 1
    return x

print(change_global())