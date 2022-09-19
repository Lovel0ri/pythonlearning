# @Time: 2022/9/19 23:34
# @Author: 李树斌
# @File : 10.4.2保存和读取用户生成的数据.py
# @Software :PyCharm
#存储用户信息
import json
username = input("请输入您的名字")

with open('username.json','w') as f:
    json.dump(username,f)
    print(f"您好,{username}")
#读取存储文件中的用户信息
filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"您好，{username}")