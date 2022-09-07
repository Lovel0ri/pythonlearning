# @Time: 2022/9/8 0:41
# @Author: 李树斌
# @File : p122练习.py
# @Software :PyCharm

#8-3 8-4
# def dingzhi_tshirt(ziyang="I love Python", type ="XL"):
#     # ziyang = input("\n您好，你的衣服需要什么字样")
#     # type = input("需要什么尺码亲？如果没有指定的话我们这里默认XL码")
#     print(f"您好，您需要定制的衣服的字样是{ziyang}尺码是{type}")
# dingzhi_tshirt(type="XXl")
#
# dingzhi_tshirt(type="XL")
#
# dingzhi_tshirt(ziyang="nmsl")

#8-5
def describe_city(city_name = "",city_belong = "加拿大"):
    print(f"{city_name}在{city_belong}")
describe_city("多伦多")
describe_city("温哥华")
describe_city("纽约","美国")