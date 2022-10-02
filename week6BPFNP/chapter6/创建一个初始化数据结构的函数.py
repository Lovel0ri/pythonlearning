# @Time: 2022/10/2 18:24
# @Author: 李树斌
# @File : 创建一个初始化数据结构的函数.py
# @Software :PyCharm
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
    return data

storage = {}
print(init(storage))
def lookup(data, label, name):
    return data[label].get(name)