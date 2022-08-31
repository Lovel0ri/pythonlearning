# @Time: 2022/8/31 22:59
# @Author: 李树斌
# @File : range()迭代固定次数.py
# @Software :PyCharm
movies = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
movies1 = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,]
def print_lol(the_list,level):
    """这个函数有一个位置参数叫"the_list",
    这可以是任何python列表（包含或者不包含嵌套列表），
    所提供列表中的各个数据项会（递归地）打印到屏幕上，而且各占一行"""

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)
#进行输出的对比
print_lol(movies,0)
print_lol(movies1,0)