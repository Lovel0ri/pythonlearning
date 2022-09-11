# @Time: 2022/9/11 0:04
# @Author: 李树斌
# @File : p149 9-5.py
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



user_1 = User("Bingbing","Chen")
user_1.greet_user()
user_1.increment_login_attempts()
user_1.login_attempt()
user_1.increment_login_attempts()

user_1.login_attempt()