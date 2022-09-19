# @Time: 2022/9/19 23:29
# @Author: 李树斌
# @File : json.dumo.load.py
# @Software :PyCharm
import json
numbers = [2,3,4,5,6]
filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)#dump接受两个参数，要存储的数据和用于存储的文件对象

with open('numbers.json') as f:
    numbers=json.load(f)
print(numbers)