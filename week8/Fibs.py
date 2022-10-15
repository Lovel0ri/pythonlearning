# @Time: 2022/10/15 15:21
# @Author: 李树斌
# @File : Fibs.py
# @Software :PyCharm

#列表、元组、字典和集合都是可迭代的对象。它们是可迭代的容器，您可以从中获取迭代器（Iterator）。
#迭代器是一个可以记住遍历的位置的对象。
#迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
#迭代器只能往前不会后退。
#迭代器有两个基本的方法：iter() 和 next()。
#字符串、列表或元组对象都可用于创建迭代器：
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

it = iter([1,2,3,4,5])
print(next(it))
print(next(it))
for i in it:
    print(i)