# @Time: 2022/10/13 0:33
# @Author: 李树斌
# @File : badPropertyExample.py
# @Software :PyCharm
class ClassWithBadProperty:
    def __init__(self):
        self.someArrtribute = 'some initial value'

    @property
    def someArrtribute(self):#这是getter方法
        #这里忘记加下划线_，将self._someArrtribute写成了someArrtribute
        #由于访问了属性（property，导致再次调用getter方法
        return self.someArrtribute

    @someArrtribute.setter
    def someArrtribute(self,value):#这是setter方法
        self._someArrtribute = value

opj = ClassWithBadProperty()
print(opj.someArrtribute)