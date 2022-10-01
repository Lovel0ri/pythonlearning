# @Time: 2022/10/1 11:25
# @Author: 李树斌
# @File : 4-1字典示例.py
# @Software :PyCharm
people = {
'Beth':{
    'phone':9102,
    'addr':'Foo drive 23'
    },
'Cecil':{
    'phone':3158,
    'addr':'Bar street 42'
    }
}
labels = {
    'phone':'phone number',
    'addr':'address'
}

#要查找电话号码还是地址
name = input('Name:')
request = input('Phone number(p) or address(a)?')

#使用正确的键
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

#仅当名字是字典包含的键时才打印消息
if name in people:
    print(f"{name}'s {labels[key]} is {people[name][key]}.")