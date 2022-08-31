# @Time : 2022/8/30  22:50
# @Author: 李树斌
# @File : if处理列表.py
# @Software : PyCharm
#创建列表
movies = ["The Holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
            ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for each_item in movies:
    #检查是否是嵌套列表
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)