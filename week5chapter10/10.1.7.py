# @Time: 2022/9/19 0:36
# @Author: 李树斌
# @File : 10.1.7.py
# @Software :PyCharm

filename = 'pi_million_digits.txt'
with open(filename) as file_project:
    lines = file_project.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
polling_activate = True
while polling_activate:
    birthday = input("请输入你的生日：")
    if birthday in pi_string:
        print("你的生日在圆周率里面")
    else:
        print("不在")
    again = input("还想玩吗？(y/n)")
    if again == "y":
        continue
    else:
        break




