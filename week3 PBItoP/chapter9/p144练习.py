# @Time: 2022/9/10 16:39
# @Author: 李树斌
# @File : p144练习.py
# @Software :PyCharm

#9-1
class Supermarket:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_supermarket(self):
        print(f"大家好，我是{self.name}")

    def open_supmarket(self):
        print(f"顾客们好，我们{self.type}中")

i_supermarket = Supermarket('华润万家','营业')
i_supermarket.describe_supermarket()
i_supermarket.open_supmarket()

#9-3
class user:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        return  full_name.title()
    def greet_user(self):
        print(f"你好，{self.describe_user()}")

my_name = user("bingbing","Chen")
print(my_name.greet_user())