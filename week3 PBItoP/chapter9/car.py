# @Time: 2022/9/11 14:38
# @Author: 李树斌
# @File : car.py
# @Software :PyCharm
"""一个可用于展示汽车的类"""
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
