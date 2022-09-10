# @Time: 2022/9/10 17:33
# @Author: 李树斌
# @File : 9.2.1Car类.py
# @Software :PyCharm

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


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

my_new_car = Car("audi","a4",2019)
print((my_new_car.get_descriptive_name()))
my_new_car.read_odometer()
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.update_odometer(15)
my_new_car.read_odometer()