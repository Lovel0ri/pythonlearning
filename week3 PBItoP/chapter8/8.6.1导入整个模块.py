# @Time: 2022/9/8 23:50
# @Author: 李树斌
# @File : 8.6.1导入整个模块.py
# @Software :PyCharm

def make_pizzas(*toppings):
    print(f"我们正在做一个包含这些配料的披萨:")
    for topping in toppings:
        print(topping)
# make_sandwitchs("芝士","新奥尔良鸡肉")
