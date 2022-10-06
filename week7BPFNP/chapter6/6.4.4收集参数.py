# @Time: 2022/10/5 17:32
# @Author: 李树斌
# @File : 6.4.4收集参数.py
# @Software :PyCharm
def print_params(*params):
    print(params)

# print_params('Testing')
# print_params(1, 2, 3)

def in_the_middle(x, *y, z):
    print(x, y, z)

in_the_middle(1, 2, 3, 4, 5, z=6)

def print_params_3(**params):
    print(params)

print_params_3(x=1, y=2, z=3)
