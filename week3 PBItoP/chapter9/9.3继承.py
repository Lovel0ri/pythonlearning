# @Time: 2022/9/11 11:50
# @Author: 李树斌
# @File : 9.3继承.py
# @Software :PyCharm


class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fill_gas = 0


    def get_descriptive_name(self):
        """反正整洁的描述性语言"""
        long_name = f"{self.year} {self.make} {self.model}"
        return  long_name.title()

    def read_odometer(self):
        """打印一条指出汽车历程的信息"""
        print(f"这车子已经行驶了{self.odometer_reading}公里")

    def update_odometer(self,km):
        """将里程表设为指定的值
        禁止回调里程表"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("不可以把里程表往回调！")
    def increment_odometer(self,km):
        #将里程表增加指定的量
        self.odometer_reading += km

    def fill_gas_tank(self):
        print(f"您的汽车还有{self.fill_gas} L油")

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

my_tesla = ElectricCar("tesla","model s",2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery_size()
"""这行代码让Python在实例my_tesla中查找属性battery，并对存储在该属性中的Battery实例调用方法describe_batter_size()"""
my_tesla.battery.get_range()