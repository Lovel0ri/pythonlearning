# @Time: 2022/9/8 14:42
# @Author: 李树斌
# @File : p127练习.py
# @Software :PyCharm

#8-6
# def city_country(city,country):
#     print(f"{city}在{country}")
#
#
# city_country("广州","中国")
#8-7
def make_album(singer,album):
    print(f"你喜欢的歌手是{singer},ta的专辑是{album}")

polling_active = True
while polling_active:
    print(f"可以告诉我你喜欢的歌手的名字和专辑名吗？\n输入q退出程序")
    s_name = input("ta的名字是：")
    if s_name == "q":
        break
    a_name = input("专辑名字是:")
    if a_name == "q":
        break
    m_album = make_album(s_name,a_name)
    print(f"{s_name}有一本专辑是{a_name}")


#8-8
