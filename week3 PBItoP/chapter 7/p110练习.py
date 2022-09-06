# @Time: 2022/9/6 20:33
# @Author: 李树斌
# @File : p110练习.py
# @Software :PyCharm

#7-4

# info_peiliao =("你的披萨要什么配料？")
# active = True
# while active:
#     info_get = input(info_peiliao)
#     if info_get == 'quit':
#         break
#     else:
#         print(f"好的，你想要的披萨配料是{info_get}")

#7-5
# age = "你几岁啊"
#
# active = True
# while active:
#     age_get = int(input(age))
#     if age_get < 3:
#         print("你好，你免费")
#     elif age_get >=3 and age_get <= 12:
#         print("给十块")
#     elif age_get >12 :
#         print("15块")
#
#     else:
#         break

#7-6
#while循环中使用条件测试
# info_peiliao =("你的披萨要什么配料？")
# active = True
# while active:
#     info_get = input(info_peiliao)
#     if info_get == 'quit':
#         active = False
#     else:
#         print(f"好的，你想要的披萨配料是{info_get}")

# info_peiliao =("你的披萨要什么配料？")
# active = True
# while active:
#     info_get = input(info_peiliao)
#     if info_get != 'quit':
#         print(f"好的，你想要的披萨配料是{info_get}")
#         active = False

x = 1
while True:
    print(x)
    x +=1