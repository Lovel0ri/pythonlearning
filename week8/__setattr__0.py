# @Time: 2022/10/15 14:28
# @Author: 李树斌
# @File : __setattr__0.py
# @Software :PyCharm

class A:
    def __init__(self, value):
        print("into __init__")
        self.value = value

    def __setattr__(self, name, value):
        print("into __setattr__")
        if value == 10:
            print("from __init__")
        object.__setattr__(self, name, value)


a = A(10)
# into __init__
# into __setattr__
# from __init__
print(a.value)
# 10
a.value = 100
# into __setattr__
print(a.value)
