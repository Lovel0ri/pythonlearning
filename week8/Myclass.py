# @Time: 2022/10/15 12:14
# @Author: 李树斌
# @File : Myclass.py
# @Software :PyCharm
# class MyClass:
#     def smeth():
#         print('This is a static method')
#     smeth = staticmethod(smeth)
#
#     def cmeth(cls):
#         print('This is a class method of',cls)
#     cmeth = classmethod(cmeth)


class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')


    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)

print(MyClass.smeth())
