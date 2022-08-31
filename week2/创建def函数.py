# @Time : 2022/8/31  12:34
# @Author: 李树斌
# @File : 创建def函数.py
# @Software : PyCharm

"""def 函数名 （参数） 参数表是可选的但是括号必不可少 :
        函数代码组"""
#创建列表
movies = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
def print_lol(thelist):
    for each_item in thelist:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)

