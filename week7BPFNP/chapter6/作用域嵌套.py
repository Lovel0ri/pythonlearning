# @Time: 2022/10/5 19:54
# @Author: 李树斌
# @File : 作用域嵌套.py
# @Software :PyCharm
# def foo():
#
#     def bar():
#         print("hello,world")
#
#     bar()
#
# foo()
def multiplier(factor):
    def multiplyByFactor(number):#multiplyByFactor是一个闭包(存储其所在作用域的函数）
        return number * factor
    return multiplyByFactor
double = multiplier(2)
print(double(5))