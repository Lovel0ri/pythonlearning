# @Time: 2022/11/9 1:38
# @Author: 李树斌
# @File : 使用列表推导计算笛卡尔积.py
# @Software :PyCharm
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)