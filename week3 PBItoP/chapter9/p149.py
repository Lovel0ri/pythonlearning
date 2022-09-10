# @Time: 2022/9/10 20:18
# @Author: 李树斌
# @File : p149.py
# @Software :PyCharm

#9-4
class Supermarket:

    def __init__(self, name, type,chifan):
        self.name = name
        self.type = type
        self.served_numbers = 10
        self.chifan = 0


    def describe_supermarket(self):
        print(f"大家好，我是{self.name}")

    def open_supmarket(self):
        print(f"顾客们好，我们{self.type}中")

    def numbers_served(self):
        print(f"已经服务过{self.served_numbers}人")

    def set_number_served(self,chifan):
        print(f"今晚的就餐人数是{self.chifan}")

    def increment_number_served(self,xinzeng):
        #设置增加的就餐人数
        self.chifan += xinzeng
    def get_describe(self):
        print(f"今晚有{self.chifan}人就餐")


supermarket = Supermarket("大润发","营业中","5")
# supermarket.numbers_served()
# supermarket.set_number_served()

supermarket.increment_number_served(30)
print(supermarket.get_describe())
supermarket.increment_number_served(10)
print(supermarket.get_describe())
# supermarket.increment_number_served(20)
# supermarket.set_number_served()