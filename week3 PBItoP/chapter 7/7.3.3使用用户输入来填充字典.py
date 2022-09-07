# @Time: 2022/9/6 23:42
# @Author: 李树斌
# @File : 7.3.3使用用户输入来填充字典.py
# @Software :PyCharm
responses = {}
polling_active = True
while polling_active:
    name = input("你叫啥啊")
    response = input("你喜欢吃啥啊")

    #将回答存储在字典中
    responses[name] = response
    #看看是否还有人参与调查
    repeat = input(f"你要邀请别人一起来参加吗？(yes/no)")
    if repeat == 'no':
        polling_active = False
print("---Poll Results---")
for name, response in responses.items():
    print(f"{name},你喜欢吃{response}")