# @Time: 2022/9/19 22:21
# @Author: 李树斌
# @File : p173.py
# @Software :PyCharm
#10-3&10-4
polling_activate =True
while polling_activate:
    new_name = str(input('请输入名字'))
    if new_name == 'quit':
        break
    reason = input('你为什么学python')
    # name = []

    name = [i for i in new_name ]
    # for i in new_name:
    #     name.append(i)
    print(f"Hello,{new_name}\n{reason}")
    with open('name.txt','a') as data:
        data.write('\n')
        for j in name:
            data.write(f"{j}")

