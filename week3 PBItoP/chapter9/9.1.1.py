# @Time: 2022/9/10 15:39
# @Author: 李树斌
# @File : 9.1.1.py
# @Software :PyCharm

class Dog:
    """一次芝士雪豹的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def shutup(self):
        "模拟芝士雪豹收到命令时蹲下"
        print(f"{self.name}闭嘴")

    def roll_over(self):
        "模拟芝士雪豹收到命令时打滚"
        print(f"{self.name}打滚")


my_dog = Dog("芝士雪豹","10")
my_dog.shutup()
my_dog.roll_over()
# print(f"我的动物朋友叫{my_dog.name}")
# print(f"我的动物朋友{my_dog.age}岁")

# print(my_dog.name)#点记法获取属性的值
#让芝士雪豹闭嘴
