# @Time: 2022/9/11 13:56
# @Author: 李树斌
# @File : p155 9-7.py
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



class Priveleges:
    def __init__(self,privileges = ["can add post", "can delete post" ,"can ban user"]):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"管理员有以下权限:{self.privileges}")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Priveleges()

bing = Admin("Bingbing","Chen")
bing.greet_user()

bing.privileges.show_privileges()
