# @Time: 2022/10/1 12:04
# @Author: 李树斌
# @File : 4-2字典方法示例.py
# @Software :PyCharm
#一个使用get()的简单数据库
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

name = input('Name:')

request = input('Phone number(p) or address(a)')
key = request

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'address'

#使用get提供默认值
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')

print(f"{name}'s {label} is {result}")