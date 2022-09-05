# @Time: 2022/9/5 17:59
# @Author: 李树斌
# @File : 6.4.3在字典中存储字典.py
# @Software :PyCharm

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last': 'curie',
        'location': 'paris',

    },
}

for users_name,users_info in users.items():
    print(f"\n Username : {users_name}")
    full_name = f"{users_info['first']} {users_info['last']}"
    location = users_info['location']


    print(f"\t Full name : {full_name.title()}")
    print(f"\tlocation: {location.title()}")