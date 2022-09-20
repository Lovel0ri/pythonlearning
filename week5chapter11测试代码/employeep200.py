# @Time: 2022/9/20 13:15
# @Author: 李树斌
# @File : employeep200.py
# @Software :PyCharm
class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self,increase=5000):
        self.salary += increase

