# @Time: 2022/9/11 14:49
# @Author: 李树斌
# @File : my_electric_car.py
# @Software :PyCharm
from car import Car
from car import ElectricCar as EC

my_tesla = EC("tesla","model s",2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery_size()
my_tesla.battery.get_range()

my_new_car = Car("audi","a4",2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading =23
my_new_car.read_odometer()
