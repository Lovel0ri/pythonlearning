# @Time: 2022/10/12 0:17
# @Author: 李树斌
# @File : 9.2.1.py
# @Software :PyCharm
class A:
    # def __init__(self,greet):
    #     self.greet = greet
    def hello(self,greet):
        # return ("Hello,Im A")
        return greet

class B(A):
    pass
    # def hello(self):
    #     return ("Hello,Im B")

a = A()
print(a.hello("你好"))#通常都是这样去调用类的方法

print(A.hello(a,'你好'))#这样去理解就能明白self的作用了


# b = B()
# print(a.hello())
# print(b.hello())