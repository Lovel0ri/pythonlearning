# @Time: 2022/9/20 1:25
# @Author: 李树斌
# @File : name_function.py
# @Software :PyCharm
#将形参移到形参列表末尾
def get_formatted_name(first,last,middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()

