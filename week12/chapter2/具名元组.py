# @Time: 2022/11/9 12:50
# @Author: 李树斌
# @File : 具名元组.py
# @Software :PyCharm
from collections import namedtuple
# 1.创建具名元组
City = namedtuple('City', 'name country population coordinates')
# 2.创建具名元组的实例
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# 3.访问具名元组的属性
# print(tokyo)
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[1])
print(City._fields)
print(tokyo._asdict())
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())#{'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': (28.613889, 77.208889)}
print(delhi)