# @Time: 2022/10/12 0:17
# @Author: 李树斌
# @File : 9.2.1.py
# @Software :PyCharm
class A:
    def hello(self):
        return ("Hello,Im A")

class B(A):
    def hello(self):
        return ("Hello,Im B")

a = A()
b = B()
print(a.hello())
print(b.hello())