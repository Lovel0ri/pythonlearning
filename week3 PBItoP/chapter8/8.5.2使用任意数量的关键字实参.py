# @Time: 2022/9/8 19:42
# @Author: 李树斌
# @File : 8.5.2使用任意数量的关键字实参.py
# @Software :PyCharm

def build_profile(first,last,**user_info):
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info

user_profile = build_profile("Bingbing","Chen",性别="男生",爱做的事="喜欢听歌",不喜欢的事="不喜欢运动")
print(user_profile)