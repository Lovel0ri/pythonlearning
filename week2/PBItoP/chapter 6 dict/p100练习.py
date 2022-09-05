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