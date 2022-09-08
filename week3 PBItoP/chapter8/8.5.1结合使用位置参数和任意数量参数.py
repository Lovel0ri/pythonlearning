# @Time: 2022/9/8 18:07
# @Author: 李树斌
# @File : 8.5.1结合使用位置参数和任意数量参数.py
# @Software :PyCharm
def make_pizza(size,*toppings):
    """打印顾客点的所有配料"""
    for topping in toppings:
        print(f"正在做{size}寸的{topping},请稍等")
make_pizza(16,"加倍芝士")
make_pizza(12,"香肠","黑松露","牛肉粒")