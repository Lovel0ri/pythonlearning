# @Time: 2022/9/5 18:23
# @Author: 李树斌
# @File : p100练习.py
# @Software :PyCharm
import json

#6-7
users={
"bingbing":{'first': 'bingbing',
            'last': 'Chen',
            'City': 'Guangzhou'},
"aeinstein":{
        'first': 'albert',
        'last': 'einstein',
        'City': 'princeton',},
"mcurie":{
        'first':'marie',
        'last': 'curie',
        'City': 'paris',}
}
for names in users.values():
    full_name = f"{names['first']} {names['last']} lives in {names['City']}"
    print(full_name)


#6-8

aeby ={
        'host': 'benny',
        'kind': 'dog'
    }
lucy ={
        'host':'Mike',
        'kind': 'cat'
    }


pets_1 = [aeby,lucy]

for pet in pets_1:
    print(pet)

#6-9
favorite_places = {
    'bingbing':['litang', 'dongfan','saojiehome'],
    'caojie':['litang','guangwai','shunde'],
    'juju':['dongguan','dongfan','chabaidao']
}
infos = []
for name,info in favorite_places.items():
    print(f"{name}'s favourite places are : {info}")
# 中大南方 ="https://www.nfu.edu.cn/ztb/index.htm"
# for page in range(27):
#     print(f"https://www.nfu.edu.cn/ztb/index{str(page)}.htm")

#6-11
cities = {
    'guangzhou':{
        'country':'China',
        'population':'18',
        'fact':'G'
    },
    'shanghai':{
        'country':'China',
        'population':'20',
        'fact':'S'
    },
    'paris':{
        'countrty':'France',
        'population':'5',
        'fact':'P'
    }
}
for city_name,info in cities.items():
    print(f"{city_name}:{info}")
