# @Time: 2022/9/19 23:47
# @Author: 李树斌
# @File : 10.4.3重构.py
# @Software :PyCharm
import json
def get_sorted_username():
    """如果存储了用户数据就去获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """问候用户，并指出名字"""
    username = get_sorted_username()
    if username:
        print(f"欢迎回来{username}")
    else:
        username = input('请输入姓名')
        with open('username.json','w') as f:
            json.dump(username,f)
            print(f'我会记得你的当你回来的时候，{username}')

greet_user()