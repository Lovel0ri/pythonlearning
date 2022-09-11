# @Time: 2022/9/11 13:29
# @Author: 李树斌
# @File : Supermarket.py
# @Software :PyCharm


#9-6
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


class IceCreamStand(Supermarket):
    def __init__(self,name,type,chifan):
        super().__init__(name,type,chifan)
        self.flavors = ["香草味","巧克力味"]

    def get_flavors(self):
        print(f"我们有以下口味的雪糕{self.flavors}")


# ice = IceCreamStand("哈根达斯","营业中",20)
# print(ice.describe_supermarket())
#
# ice.get_flavors()



