# @Time: 2022/10/15 14:08
# @Author: 李树斌
# @File : setattr_getattr.py
# @Software :PyCharm
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width,self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width,self.height
        else:
            raise AttributeError

r = Rectangle()
r.width = 10
r.height = 5
