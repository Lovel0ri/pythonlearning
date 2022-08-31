# @Time : 2022/8/31  16:54
# @Author: 李树斌
# @File : nester1.py
# @Software : PyCharm
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

