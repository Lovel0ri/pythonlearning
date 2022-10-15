# @Time: 2022/10/13 0:22
# @Author: 李树斌
# @File : property.py
# @Software :PyCharm
#property

class ClassWithProperties:
    def __init__(self):
        self.someAttribute = 'some inital value'

    @property
    def someArrtribute(self):#这是getter方法
        return self._someAttribute

    @someArrtribute.setter
    def someArrtribute(self,value):#这是setter方法
        self._someArrtribute = value

    @someArrtribute.deleter
    def someArrtribute(self):#这是deleter方法
        del self._someArrtribute

obj = ClassWithProperties()
print(obj.someAttribute)
