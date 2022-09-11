# @Time: 2022/9/11 14:39
# @Author: 李树斌
# @File : my_car.py
# @Software :PyCharm
from  car import Car

my_new_car = Car("audi","a4",2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading =23
my_new_car.read_odometer()