# @Time: 2022/11/3 20:22



#健身房管理系统
class Customer:
    def __init__(self):
        # self.name = name
        self.money = 0
        self.card = None
        #会员卡的次数
        self.card_time = None
        #消费记录
        self.record = []
        #创建姓名和密码的字典
        self.name_password = {}


    #注册
    def register(self):
        #账号密码不能为空

        name = input("注册页面\n请输入姓名：")
        #输入不能为空
        while True:
            if name:
                break
            else:
                name = input("注册页面\n请输入姓名：")
        password = input("请输入密码：")
        while True:
            if password:
                break
            else:
                password = input("请输入密码：")
        self.name_password[name] = password
        self.name = name
        return "注册成功！"

    #判断用户注册没有
    def is_register(self):
        if self.name_password:
            return True
        else:
            return False

    #登陆之前判断用户注册没有
    def login(self):
        is_register = self.is_register()
        if is_register:
            name = input("登陆页面\n请输入姓名：")
            password = input("请输入密码：")
            if name in self.name_password:
                if password == self.name_password[name]:
                    return "登陆成功！"

                else:
                    return "密码错误！"
            else:
                return "用户不存在！"

        else:
            return "请先注册！"


    #存钱

    def save_money(self):
        is_register = self.is_register()
        if is_register:
            money = int(input("请输入要存的金额："))
            self.money += money
            print("存钱成功！")
            return f"余额 :{self.money}"


    def buy_card(self):
        is_login = self.login()
        print(is_login)
        if is_login:
            card_pirce = 100
            # 检查余额是否足够
            yse_or_no = input("是否购买/续费会员卡？（y/n）")
            if yse_or_no == "y":
                if self.money >= card_pirce:
                    self.money -= card_pirce
                    self.card = "会员卡"
                    # 添加消费记录
                    self.record.append(f"{self.name}办理/续费了{self.card}:{card_pirce}元")
                    return "购买/续费成功！"
                else:
                    return "余额不足！"
            if yse_or_no == "n":
                return "退出！"

        else:
            return "请先注册！"




    #消费记录的查询
    def show_record(self):
        is_login = self.login()
        if is_login:
            record = [i for i in self.record]
            if record:
                for i in record:
                    return i
            else:
                return "无消费记录！"



    #个人信息
    def show_info(self):
        is_register = self.is_register()
        if is_register:
            print("姓名：", self.name)
            print("余额：", self.money)
            print("会员卡：", self.card)
            print("会员卡次数：", self.card_time)
            return f"消费记录: {self.record}"

        else:
            return "请先注册！"


    #个人信息的修改
    def change_info(self):
        is_register = self.is_register()
        if is_register:
            print("1.修改姓名")
            print("2.修改密码")
            print("3.退出")
            num = int(input("请输入要修改的选项："))
            if num == 1:
                name = input("请输入新的姓名：")
                self.name_password[name] = self.name_password[self.name]
                print("修改成功！")
            elif num == 2:
                password = input("请输入新的密码：")
                self.password = password
                print("修改成功！")
            elif num == 3:
                return
            else:
                print("输入错误！")
        else:
            print("请先注册！")

    def __str__(self):
        return self.name


# cust1 = Customer()
# # print(cust1.register())
# # print(cust1.login())
# #
# # print(cust1.save_money())
# # print(cust1.buy_card())
# # print(cust1.show_record())
# # print(cust1.show_info())



class manager:
    def __init__(self):
        self.customer_list = []
        self.card_list = []

    def show_menu(self):
        print("1.添加会员")
        print("2.添加卡")
        print("3.会员充值")
        print("4.办理卡")
        print("5.会员信息")
        print("6.退出")

    def add_customer(self):
        name = input("请输入会员姓名：")
        customer = Customer(name)
        self.customer_list.append(customer)
        print("添加成功")

    def add_card(self):
        name = input("请输入卡名：")
        money = int(input("请输入卡的金额："))
        card = Card(name, money)
        self.card_list.append(card)
        print("添加成功")

    def recharge(self):
        name = input("请输入会员姓名：")
        money = int(input("请输入充值金额："))
        for customer in self.customer_list:
            if customer.name == name:
                customer.money += money
                print("充值成功")
                return
        print("没有此会员")

    def issue_card(self):
        name = input("请输入会员姓名：")
        card_name = input("请输入卡名：")
        for customer in self.customer_list:
            if customer.name == name:
                for card in self.card_list:
                    if card.name == card_name:
                        customer.buy_card(card)
                        print("办理成功")
                        return
                print("没有此卡")
                return
        print("没有此会员")

    def show_customer(self):
        name = input("请输入会员姓名：")
        for customer in self.customer_list:
            if customer.name == name:
                customer.show_info()
                return
        print("没有此会员")

    def run(self):
        while True:
            self.show_menu()
            try:
                num = int(input("请输入功能序号："))
            except Exception as e:
                print("输入错误")
                continue
            if num == 1:
                self.add_customer()
            elif num == 2:
                self.add_card()
            elif num == 3:
                self.recharge()
            elif num == 4:
                self.issue_card()
            elif num == 5:
                self.show_customer()
            elif num == 6:
                break
            else:
                print("输入有误")


#教练
class Coach:
    def __init__(self, name):
        self.name = name
        self.customer_list = []

    def add_customer(self, customer):
        self.customer_list.append(customer)

    def show_info(self):
        print("教练名：", self.name)
        for customer in self.customer_list:
            print(customer)

    def __str__(self):
        return self.name

    def show_info(self):
        print("姓名：", self.name)
        print("卡：", end="")
        for card in self.card_list:
            print(card, end=" ")
        print()

    def __str__(self):
        return self.name


def main():
    cust = Customer()

    print(cust.register())


while True:

    print("1.教练")
    print("2.会员")
    print("3.管理员")
    print("4.退出")
    try:
        num = int(input("请输入功能序号："))
    except Exception as e:
        print("输入错误")
        continue
    if num == 1:
        coach = Coach()
        coach.run()
    elif num == 2:
        cust = Customer()
        cust.register()
        if cust.is_register():
            need = input("是否需要登录？(y/n)")
            if need == "y":
                cust.login()
                print("登录成功")
                while True:
                    print("1.充值")
                    print("2.办理卡")
                    print("3.查看记录")
                    print("4.查看个人信息")
                    print("5.退出")
                    try:
                        num = int(input("请输入功能序号："))
                    except Exception as e:
                        print("输入错误")
                        continue
                    if num == 1:
                        cust.save_money()
                    elif num == 2:
                        cust.buy_card()
                    elif num == 3:
                        cust.show_record()
                    elif num == 4:
                        cust.show_info()
                    elif num == 5:
                        break
                    else:
                        print("输入有误")

        else:
            print("请先注册")
    elif num == 3:
        manager = Manager()
        manager.run()
    elif num == 4:
        break
    else:
        print("输入有误")