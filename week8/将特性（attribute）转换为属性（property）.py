# @Time: 2022/10/12 23:49
# @Author: 李树斌
# @File : 将特性（attribute）转换为属性（property）.py
# @Software :PyCharm
class ClassWithRegularAttributes:
    def __init__(self,someParameter):
        self.someAttributes = someParameter

obj = ClassWithRegularAttributes('some initial value')
print(obj.someAttributes)

obj.someAttributes = ('change value')
print(obj.someAttributes)

del obj.someAttributes#删除someAttributes特性
try:
    print(obj.someAttributes)
except Exception as e:
    print(e)




