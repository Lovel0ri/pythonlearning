# @Time: 2022/9/8 15:52
# @Author: 李树斌
# @File : 8.4传递列表.py
# @Software :PyCharm

def greet_users(names):
    for name in names:
        msg = f"你好，{name}"
        print(msg)

users_name = ['冰冰','骚杰','juju']
greet_users(users_name)