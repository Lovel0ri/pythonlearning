# @Time : 2022/8/31  17:40
# @Author: 李树斌
# @File : 测试nester0模块.py
# @Software : PyCharm

#暂时有bug没修复，无法调用nester1(已修复）
import nester1
# def print_lol(the_list,indent = False,level=0):
#     """这个函数有一个位置参数叫"the_list",
#     这可以是任何python列表（包含或者不包含嵌套列表），
#     所提供列表中的各个数据项会（递归地）打印到屏幕上，而且各占一行"""
#     """update:1.2.0增加缺省参数，将函数调用的负责缩进的参数改为可选的参数"""
#
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item,indent,level+1)
#         else:
#             if indent:
#                 for tab_stop in range(level):
#                     print("\t"*level, end='')
#                 print(each_item)

movies = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
nester1.print_lol(movies,1)