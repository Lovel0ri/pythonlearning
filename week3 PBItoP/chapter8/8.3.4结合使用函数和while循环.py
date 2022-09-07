# @Time: 2022/9/8 1:55
# @Author: 李树斌
# @File : 8.3.4结合使用函数和while循环.py
# @Software :PyCharm
def get_formatted_name(first_name,last_name,middle_name =''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\n可以告诉我你的名字吗")
    print(f"输入q退出程序")

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"你好,{f_name} {l_name}")