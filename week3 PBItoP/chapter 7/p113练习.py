# @Time: 2022/9/7 22:01
# @Author: 李树斌
# @File : p113练习.py
# @Software :PyCharm
#7-8
# sandwitch_orders = ["青瓜芝士三文治","芝士火腿三文治","芝士蛋三文治","烟熏牛肉三文治","烟熏牛肉三文治","烟熏牛肉三文治"]
# finished_sandwitches = []
# while sandwitch_orders:
#     for sandwitch_order in sandwitch_orders:
#         print(f"我做好你的{sandwitch_order}了")
#         finished_sandwitch = sandwitch_orders.pop()
#         finished_sandwitches.append(finished_sandwitch)
#         if sandwitch_order == "烟熏牛肉三文治":
#             while "烟熏牛肉三文治" in sandwitch_orders:
#                 sandwitch_orders.remove("烟熏牛肉三文治")
# print(f"{finished_sandwitches}都做好啦")
# #检查烟熏牛肉三文治不存在于列表中
# print(sandwitch_orders)

#7-10
responses = {}
polling_active = True
while polling_active:
    name = input("您好，怎么称呼您")
    response = input("如果给你一张免费的机票，你想去世界上的哪里?")
    responses[name] = response
    for i_name,i_response in responses.items():
        print(f"{i_name}先生，您确定要去{i_response}")
        response_again = input("(yes/no)")
        if response_again == "no":
            responses = {}

            response = input("如果给你一张免费的机票，你想去世界上的哪里?（最后一次确定的机会）")
            responses[name] = response
            print(f"您已经确定要去{response}")
            polling_active = False
        else:
            polling_active=False



