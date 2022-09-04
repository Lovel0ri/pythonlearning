# @Time: 2022/9/4 14:14
# @Author: 李树斌
# @File : p206继承python的内置list类.py
# @Software :PyCharm

class NameList(list):
    def __init__(self,a_name):
        list.__init__([])
        self.name = a_name

johnny = NameList('John Paul Jones')
print(type(johnny))