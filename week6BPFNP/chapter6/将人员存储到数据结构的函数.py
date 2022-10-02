# @Time: 2022/10/2 18:39
# @Author: 李树斌
# @File : 将人员存储到数据结构的函数.py
# @Software :PyCharm
# 初始化数据结构的函数，用于存储人员信息
def init(data):
    data["first"] = {}
    data["middle"] = {}
    data["last"] = {}
    return data


# 查找人员信息的函数
def lookup(data, label, name):
    #如果键存在，返回键对应的值，否则返回None
    return data[label].get(name)


# 存储人员信息的函数
def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, "")
    #将'first'、'middle'、'last'作为键，将名字作为值
    labels = "first", "middle", "last"
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


data = {}
init(data)

store(data, "Magnus Lie Hetland")
print(lookup(data, "middle", "Lie"))
print(lookup(data, "middle", "Bob"))
