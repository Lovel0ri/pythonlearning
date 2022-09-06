# @Time: 2022/9/6 19:36
# @Author: 李树斌
# @File : 7.1input.py
# @Software :PyCharm

# nameg = "How r u?"
# nameg += "May I have your name?"
# name = input(nameg)
# print(f"\nHello,{name}")
#

age = input("How old r u?")
age = int(age)
if age < 18 :
    print("你还没成年")
else:
    print("恭喜你，你成年了")