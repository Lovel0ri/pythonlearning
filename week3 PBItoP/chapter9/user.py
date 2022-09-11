# @Time: 2022/9/11 15:03
# @Author: 李树斌
# @File : user.py
# @Software :PyCharm
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        return  full_name.title()
    def greet_user(self):
        print(f"你好，{self.describe_user()}")

    def login_attempt(self):
        print(f"您的登陆次数是{self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



