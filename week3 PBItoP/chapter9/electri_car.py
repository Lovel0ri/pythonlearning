# @Time: 2022/9/11 14:54
# @Author: 李树斌
# @File : electri_car.py
# @Software :PyCharm
from car import Car
class Battery:
    """一次模拟电动车汽车电瓶的简单尝试"""

    """初始化电瓶的属性"""
    def __init__(self,battery_size = 75):
        self.battery_size = 75

    def describe_battery_size(self):
        """打印一条描述电瓶容量的信息"""
        print(f"这辆车拥有{self.battery_size}--kWh 的电瓶容量")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 250
        elif self.battery_size == 100:
            range = 310

        print(f"您的车子的续航里程是{range}")

class ElectricCar(Car):
    """电动汽车的独到之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("您好，电动汽车没有油箱")
