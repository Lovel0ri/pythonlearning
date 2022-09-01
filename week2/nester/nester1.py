# @Time : 2022/8/31  16:54
# @Author: 李树斌
# @File : nesterbing.py
# @Software : PyCharm
import sys


# def print_lol(the_list):
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item)
#         else:
#             print(each_item)
def print_lol(the_list,indent = False,level=0,fh=sys.stdout):
    """这个函数有一个位置参数叫"the_list",
    这可以是任何python列表（包含或者不包含嵌套列表），
    所提供列表中的各个数据项会（递归地）打印到屏幕上，而且各占一行"""
    """update:1.2.0增加缺省参数，将函数调用的负责缩进的参数改为可选的参数"""

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t"*level, end='',file=fh)
            print(each_item,file=fh)

