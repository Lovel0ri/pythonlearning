# @Time: 2022/9/11 0:04
# @Author: 李树斌
# @File : p149 9-5.py
# @Software :PyCharm

class user:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.loginattempts = 0

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        return  full_name.title()
    def greet_user(self):
        print(f"你好，{self.describe_user()}")

    def login_attempts(self):
        print(f"您的登陆次数是{self.loginattempts}")

    def increment_login_attempts(self):
        self.loginattempts += 1

    def reset_login_attempts(self):
        self.loginattempts = 0