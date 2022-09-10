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