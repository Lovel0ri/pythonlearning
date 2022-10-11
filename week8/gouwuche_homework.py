# @Time: 2022/10/11 17:43
# @Author: 李树斌
# @File : gouwuche_homework.py
# @Software :PyCharm

# 1.0.0使用列表，单个购买
# goodslist = ["1:短袖 30元","2:裤子 40元","3:短裙 60元"]
# goodsprice = [30,40,60]
# while True:
#     balance = input("请输入您的余额"' (退出请输入q):')
#     if balance == "q":
#         break
#     print(f"{goodslist}\n")
#     choose_goods = input("请输入商品编号进行商品的购买")
#
#     num = int(choose_goods)
#     goodschosen_price = goodsprice[num-1]
#     goodschosen_list = goodslist[num-1]
#     print(f"商品总价是{goodschosen_price}")
#     if int(balance) >= goodschosen_price:
#         print("购买成功")
#     elif int(balance) < goodschosen_price:
#         print("购买失败")
#     balance = int(balance)
#     balance -= goodschosen_price
#     print(f"您购买的商品:{goodschosen_list}\n您还有{balance}")
#     break


#2.0.0使用字典
# goods = {
#     1:{
#         "good_name":"短袖",
#         "price":30,
#     },
#     2:{
#         "good_name":"裤子",
#         "price":40,
#     },
#     3:{
#         "good_name":"短裙",
#         "price":60
#     }
# }
#
# while True:
#     balance = int(input("请输入您的余额"' (退出请输入q):'))
#     if balance == "q" or balance == '':
#         break
#
#     for goods_id,goodsinfo in goods.items():
#         print(f"{goods_id}:{goodsinfo}")
#
#     input_goodsid_chosen = input("请输入商品编号进行商品的购买,用逗号隔开")
#     goodsid_chosen = [int(i) for i in input_goodsid_chosen.split(",")]
#
#     total_goods_chosen = []
#     goods_price = 0
#
#     for good_id in goodsid_chosen:
#         total_goods_chosen.append(goods[good_id]["good_name"])
#         goods_price += goods[good_id]['price']
#     print(total_goods_chosen)
#     if balance>=goods_price  :
#         print("购买成功")
#     else:
#         print("购买失败，余额不足")
#     print(f"您购买的商品和金额是:{','.join(total_goods_chosen)} {goods_price}")
#

#3.0.0创建过程


def show_goods():
    goods = {
        1: {
            "good_name": "短袖",
            "price": 30,
        },
        2: {
            "good_name": "裤子",
            "price": 40,
        },
        3: {
            "good_name": "短裙",
            "price": 60
        }
    }
    return goods





def select_goods(*goods_chosen):
    goods = {
        1: {
            "good_name": "短袖",
            "price": 30,
        },
        2: {
            "good_name": "裤子",
            "price": 40,
        },
        3: {
            "good_name": "短裙",
            "price": 60
        }
    }

    balance = input("请输入余额:")
    if balance == 'q' or balance is None:
        return select_goods()


    goods_chosen = list(goods_chosen)
    total_goods_chosen = []
    goods_price = []
    for goods_id in goods_chosen:
        total_goods_chosen.append(goods[goods_id]["good_name"])
        goods_price.append(goods[goods_id]['price'])
    balance = int(balance)
    goods_price = sum(goods_price)
    if balance >= goods_price:
        balance -= goods_price
        print("购买成功")
    else:
        print("购买失败，余额不足")

    return f"您购买的商品和金额是:{','.join(total_goods_chosen)} {goods_price}\n您支付宝余额是{balance}"


print(select_goods(1,2))

















