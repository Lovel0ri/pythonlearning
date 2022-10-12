# @Time: 2022/10/12 22:20
# @Author: 李树斌
# @File : 高阶函数.py
# @Software :PyCharm
def callItTwice(func,*args,**kwargs):
    func(*args)
    func(*args)

print(callItTwice(print,'hello,world'))