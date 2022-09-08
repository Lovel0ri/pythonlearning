# @Time: 2022/9/8 17:52
# @Author: 李树斌
# @File : 8.5传递任意数量的实参.py
# @Software :PyCharm

#形参名*toppings中的星号让Python创建一个名为toppings的空元组，将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    for topping in toppings:
        print(f"正在做{topping},请稍等")
make_pizza("加倍芝士")
make_pizza("香肠","黑松露","牛肉粒")