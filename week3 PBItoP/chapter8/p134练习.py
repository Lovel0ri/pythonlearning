# @Time: 2022/9/8 22:36
# @Author: 李树斌
# @File : p134练习.py
# @Software :PyCharm

#8-12
def make_sandwitchs(*toppings):
    print(f"我们正在做一个包含这些配料的披萨:")
    for topping in toppings:
        print(topping)
make_sandwitchs("芝士","新奥尔良鸡肉")

#8-13
def build_profile(first,last,**user_info):
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info
user_profile = build_profile("Bingbing","Chen",性别="男生",爱做的事="喜欢听歌",不喜欢的事="不喜欢运动")
print(user_profile)

#8-14
def make_car(zhizaoshang,xinghao,**car_infos):
    car_infos["制造商"] = zhizaoshang
    car_infos["型号"] = xinghao
    return car_infos
car_info = make_car("啊冰造车厂","X5",额外信息="两箱的",引擎="油电混合")
print(car_info)