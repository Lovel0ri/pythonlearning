# @Time: 2022/11/9 20:55

import config

#酒店管理系统的设计

class single_commonroom:
    #标准单人房
    def __init__(self,room_number):
        self.room_number = room_number
        self.room_type = "普通房"
        self.room_price = "100"
        self.room_status = "空闲"
        self.rent_time = 0

    #房间信息
    def room_info(self):
        print("房间号：",self.room_number,"房间类型：",self.room_type,"房间价格：",self.room_price,"房间状态：",self.room_status)

class double_commonroom(single_commonroom):
    #标准双人房
    def __init__(self,room_number):
        self.room_number = room_number
        self.room_type = "普通房"
        self.room_price = "200"
        self.room_status = "空闲"
        self.rent_time = 0

class single_deluxeroom(single_commonroom):
    #豪华单人房
    def __init__(self,room_number):
        self.room_number = room_number
        self.room_type = "豪华房"
        self.room_price = "300"
        self.room_status = "空闲"
        self.rent_time = 0


class double_deluxeroom(single_commonroom):
    #豪华双人房
    def __init__(self,room_number):
        self.room_number = room_number
        self.room_type = "豪华房"
        self.room_price = "400"
        self.room_status = "空闲"
        self.rent_time = 0


class manager:
    def __init__(self,):
        self.manager_name = config[manager_name]
        self.manager_password = config[manager_password]

    #账户的登陆
    def login(self):
        name = input('请输入管理员账户：')
        password = input('请输入管理员密码：')
        if name == self.manager_name and password == self.manager_password:
            print('登陆成功')
            return True
        else:
            print('登陆失败')
            return False

    #雇佣员工
    def hire(self):
        name = input('请输入员工姓名：')
        password = input('请输入员工密码：')
        num = len(config.waiter_all) + 1
        config.waiter_all[num] = {'waiter_name':name,'waiter_password':password}
        print('雇佣成功')


    #解雇员工
    def fire(self):
        num = input('请输入员工编号：')
        if num in config.waiter_all:
            #再次确认
            sure = input('是否确认解雇该员工？(y/n)')
            if sure == 'y':
                del config.waiter_all[num]
                print('解雇成功')
            else:
                print('取消解雇')
        else:
            print('该员工不存在')



#前台服务员
class waiter:
    # 读取config文件中的waiter_all
    def __init__(self):
        self.waiter_name = None
        self.waiter_password = None

    #注册
    def register(self):
        name = input('请输入姓名：')
        if name in config.waiter_all:
            print('该员工已存在')
            return False
        else:
            password = input('请输入密码：')
            num = len(config.waiter_all) + 1
            config.waiter_all[num] = {'waiter_name':name,'waiter_password':password}
            print('注册成功')
            return True

    #登陆
    def login(self):
        name = input('请输入员工账户：')
        password = input('请输入员工密码：')
        #判断
        if name == self.waiter_name and password == self.waiter_password:
            print('登陆成功')
            return True
        else:
            print('登陆失败')
            return False

    #查看房间信息
    def check_room(self):
        self.room_all = [single_commonroom, double_commonroom, single_deluxeroom, double_deluxeroom]
        print('房间信息如下：')
        #遍历房间列表
        for room in config.room_all:
            room.room_info()
            #将房间信息嵌套成字典
            room_info = {'room_number':room.room_number,'room_type':room.room_type,'room_price':room.room_price,'room_status':room.room_status}
            #将字典添加到列表中
            config.room_info.append(room_info)
        return config.room_info
        # 预定房间

    def order_room(self):
        # 判断是否登陆
        if self.login():
            # 获取消费积分
            self.consumption = self.check_consumption()
            # 打印所有的房间种类和价格
            for i in config.room_all:
                for j in range(len(config.room_all[i])):
                    # 如果消费积分大于0
                    if self.consumption > 10:
                        # 打印房间种类和减去消费积分后的价格,10元封顶
                        print(f"{j}:{i} {config.room_all[i][j] - 10}")
                        # 消费积分减去10
                        self.consumption -= 10
                    else:
                        # 打印房间种类和价格
                        print(f"{j}:{i} {config.room_all[i][j]}")
            # 选择房间
            rent_time = input(input('请输入入住多少晚：'))
            room_num = int(input('请选择房间(编号)：'))
            #根据编号获取房间
            room_type = self.room_all[room_num]
            #根据房间种类随机生成房间号
            if room_num == 0:
                room_number = random.randint(100, 200)
            # 判断房间是否存在
            if room_type in config.room_all:
                # 判断房间是否为空闲
                if config.room_all[room_type][room_num].room_status == '空闲':
                    # 判断消费积分是否大于0
                    if self.consumption > 10:
                        # 房间价格减去消费积分
                        config.room_all[room_type][room_num].room_price -= 10
                        # 消费积分减去10
                        self.consumption -= 10
                    # 房间状态改为已入住
                    config.room_all[room_type][room_num].room_status = '已入住'
                    # 房间入住时间
                    config.room_all[room_type][room_num].rent_time = rent_time

                    print('预定成功')
                else:
                    print('该房间已被预定')

            # 判断是否已经被预定
            # if config.room_all[room_num][status] == '空闲':
                # # 根据房间号获取房间种类
                # config.room_all[room_num][status] = '预定'
                # config.room_all[room_num][rent_time] = rent_time
                # config.order_all[self.guest_name][order_room] = room_num
                # # config.order_all[self.guest_name][order_roomtype] = room_type暂未实现
                # config.order_all[self.guest_name][order_time] = rent_time
                # config.order_all[self.guest_name][order_service] = self.need_service
                # # 随机写入五位数的订单号
                # config.order_all[self.guest_name][order_id] = random.randint(10000, 99999)
                # # 添加到消费记录，房间号，入住天数，价格
                # config.consumption_all[self.guest_name][consumption].append(
                #     [room_num, rent_time, config.room_all[room_num][price]])

                print(f"预定成功，订单号为{config.order_all[self.guest_name][order_id]}")
            else:
                print('该房间已经被预定')

    #获取用户反馈
    def get_feedback(self):


    #取消预定
    def cancel_order(self):
        #输入订单号
        order_num = input('请输入订单号：')
        if order_num in config.order_all:
            #再次确认
            sure = input('是否确认取消该订单？(y/n)')
            if sure == 'y':
                #将订单状态改为取消
                config.order_all[order_num]['order_status'] = '取消'
                print('取消成功')
            else:
                print('取消取消')
        else:
            print('该订单不存在')

    #退房
    def check_out(self):
        #输入订单号
        order_num = input('请输入订单号：')
        if order_num in config.order_all:
            #再次确认
            sure = input('是否确认退房？(y/n)')
            if sure == 'y':
                #将订单状态改为退房
                config.order_all[order_num]['order_status'] = '退房'
                print('退房成功')
            else:
                print('取消退房')
        else:
            print('该订单不存在')

    #暂未实现
    #查看客户需要的services
    # def check_services(self):
    #     print('客户需要的服务如下：')
    #     for service in config.service_all:
    #         service.service_info()
    #         #将服务信息嵌套成字典
    #         service_info = {'service_name':service.service_name,'service_price':service.service_price}
    #         #将字典添加到列表中
    #         config.service_info.append(service_info)
    #
    #     return config.service_info

class room_manager:
    def __init__(self):
        self.name = None
        self.password = None

    #注册
    def register(self):
        name = input('请输入您的姓名：')
        # 判断是否已经注册
        if name in config.room_manager_all:
            print('您已经注册过了')
            return False
        else:
            password = input('请输入您的密码：')
            # len()函数返回字典的长度
            num = len(config.room_manager_all) + 1
            config.room_manager_all[num] = {'name': name, 'password': password}
            print('注册成功')

    #登陆
    def login(self):
        name = input('请输入您的姓名：')
        password = input('请输入您的密码：')
        #判断
        if name == self.name and password == self.password:
            print('登陆成功')
            return True
        else:
            print('登陆失败')
            return False

    #查看房间信息
    def check_room(self):
        #调用waiter类的check_room方法
        waiter().check_room()
        return config.room_info




#客人
class guest:
    #读取config文件中的guest_all
    def __init__(self):
        self.guest_name = config[guest_all][guest_num][guest_name]
        self.guest_password = config[guest_all][guest_num][guest_password]
        self.guest_phone = config[guest_all][guest_num][guest_phone]
        self.need_service = config[guest_all][guest_num][need_service]

    #注册
    def register(self):
        name = input('请输入姓名：')
        password = input('请输入密码：')
        phone = input('请输入手机号：')

        #判断是否已经注册
        if name in config.guest_all:
            print('该用户已经注册')
        else:
            num = len(config.guest_all) + 1
            config.guest_all[num] = {'guest_name':name,'guest_password':password,'guest_phone':phone}
            #初始化消费记录列表
            config.consumption_all[num][consumption] = []
            print('注册成功')

    #登陆
    def login(self):
        name = input('请输入账户：')
        password = input('请输入密码：')
        #判断
        if name == self.guest_name and password == self.guest_password:
            print('登陆成功')
            return True
        else:
            print('登陆失败')
            return False

    #修改个人情况
    def change_info(self):
        #判断是否登陆
        if self.login():
            #再次确认
            sure = input('是否确认修改个人信息？(y/n)')
            if sure == 'y':
                password = input('请输入密码：')
                phone = input('请输入手机号：')
                #修改
                self.guest_password = password
                self.guest_phone = phone
                print('修改成功')
            else:
                print('取消修改')

    #消费记录查询
    def check_consumption(self):
        self.consumption = config.consumption_all[self.guest_name][consumption]
        return self.consumption


    #统计消费记录积累积分
    def count_score(self):
        #获取消费记录
        self.consumption = self.check_consumption()
        #消费一元积一分
        self.score = 0
        for i in self.consumption:
            self.score += i[2]
        return self.score

    #续订房间
    def renew_room(self):
        #判断是否登陆
        if self.login():
            #询问是否需要续订
            sure = input('是否需要续订？(y/n)')
            if sure == 'y':
                #如果需要，输入续订天数
                rent_time = int(input('请输入续订天数：'))
                #根据积分减去房间价格打印出来
                self.score = self.count_score()
                #如果积分大于10
                if self.score > 10:
                    #打印房间种类和减去消费积分后的价格,10元封顶
                    print('房间种类：{}，价格：{}'.format(config.room_all[room_num][room_type],config.room_all[room_num][price] - 10))
                    #消费积分减去10
                    self.score -= 10
                else:
                    #打印房间种类和价格
                    print('房间种类：{}，价格：{}'.format(config.room_all[room_num][room_type],config.room_all[room_num][price]))

                #修改rent_time
                for i in config.order_all[self.guest_name]:
                    config.room_all[i][rent_time] += rent_time
                    #修改消费记录
                    config.consumption_all[self.guest_name][consumption][-1][1] += rent_time
                    #修改积分
                    config.consumption_all[self.guest_name][consumption][-1][2] += config.room_all[i][price] * rent_time
                print('续订成功')
            else:
                print('取消续订')

    #入住需求的服务
    def need_service(self):
        self.services = ["早餐送到房间(30元)","代烫衣服(20元)"]
        self.services_price = [30,20]
        #判断是否登陆
        if self.login():
            sure = input('是否需要服务？(y/n)')
            if sure == 'y':
                for i in enumerate(self.services):
                    print(f"{i[0]} {i[1]}")
                #选择服务
                service_num = int(input('请选择服务(编号)：'))
                #修改消费记录
                config.consumption_all[self.guest_name][consumption][-1][1] += self.services_price[service_num]
                #写入房间号和服务到config.order_all
                config.order_all[self.guest_name][order_service].append([config.order_all[self.guest_name][order_room][-1],self.services[service_num]])
                print('服务成功')
            else:
                print('取消服务')

    #跟前台反应需求
    def need_feedback(self):
        #判断是否登陆
        if self.login():
            #输入反馈
            feedback = input('请输入反馈：')
            #写入反馈到config.feedback_all



#初始化所有房间
def init_room():
    room_all = [single_commonroom, double_commonroom, single_deluxeroom, double_deluxeroom]
    pass





