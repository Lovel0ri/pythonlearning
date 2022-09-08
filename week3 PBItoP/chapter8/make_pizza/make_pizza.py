# @Time: 2022/9/9 0:03
# @Author: 李树斌
# @File : make_pizza.py
# @Software :PyCharm
def make_pizza(*toppings):
    print(f"我们正在做一个包含这些配料的披萨:")
    for topping in toppings:
        print(topping)