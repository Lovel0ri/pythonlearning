# @Time: 2022/9/11 15:19
# @Author: 李树斌
# @File : pri and admin.py
# @Software :PyCharm
from user import User
class Priveleges:
    def __init__(self,privileges = ["can add post", "can delete post" ,"can ban user"]):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"管理员有以下权限:{self.privileges}")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Priveleges()
