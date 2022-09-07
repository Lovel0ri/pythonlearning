# @Time: 2022/9/8 1:27
# @Author: 李树斌
# @File : 8.3返回值.py
# @Software :PyCharm

def get_formatted_name(first_name,last_name,middle_name =''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('Jimi','hendrix','hooker')
print(musician)
