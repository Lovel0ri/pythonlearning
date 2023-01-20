# @Time: 2022/11/9 20:55
from info import *
#酒店管理系统的设计
class single_commonroom:
    #标准单人房
    def __init__(self,room_number):
        self.room_number = room_number
        self.room_type = "普通房"
        self.room_price = "100"
        self.room_status = "空闲"
        self.rent_time = 0

    # #房间信息
    # def room_info(self):
    #     print("房间号：",self.room_number,"房间类型：",self.room_type,"房间价格：",self.room_price,"房间状态：",self.room_status)

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


class Manager:
    def __init__(self,):
        self.manager_name = data['manager_name']
        self.manager_password = data['manager_password']

    #账户的登陆
    def login(self):
        name = input('请输入经理账户：')
        password = input('请输入经理密码：')
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
        num = len(waiter_all) + 1
        waiter_all[num] = {'waiter_name':name,'waiter_password':password}
        print('雇佣成功')
        print('员工编号：',num,'员工姓名：',name,'员工密码：',password)


    #解雇员工
    def fire(self):
        num = int(input('请输入员工编号：'))
        if num in waiter_all:
            #再次确认
            sure = input('是否确认解雇该员工？(y/n)')
            if sure == 'y':
                del waiter_all[num]
                print('解雇成功')
            else:
                print('取消解雇')
        else:
            print('该员工不存在')
    #查看所有waiter员工信息
    def check_waiter(self):
        for i in waiter_all:
            print('员工编号：',i,'员工姓名：',waiter_all[i]['waiter_name'])



#前台服务员
class Waiter:
    def __init__(self):
        self.waiter_name = None
        self.waiter_password = None

    #注册
    def register(self):
        name = input('请输入姓名：')
        if name in waiter_all:
            print('该员工已存在')
            return False
        else:
            password = input('请输入密码：')
            num = len(waiter_all) + 1
            waiter_all[num] = {'waiter_name':name,'waiter_password':password}
            print('注册成功')
            return True

    #登陆
    def login(self):
        name = input('请输入员工账户：')
        password = input('请输入员工密码：')
        #获取waiter_all中的员工信息
        for num in waiter_all:
            if name == waiter_all[num]['waiter_name'] and password == waiter_all[num]['waiter_password']:
                print('登陆成功')
                self.waiter_name = name
                self.waiter_password = password
                return True

    #查看房间信息
    def check_room(self):
        print('房间信息如下：')
        rooms = room_all.keys()
        #遍历所有房间
        for room in rooms:
            try:
                print('房间号：', room_all[room].room_number, '房间类型：', room_all[room].room_type, '房间价格：',
                      room_all[room].room_price, '房间状态：', room_all[room].room_status)
            except:
                print('暂未有房间信息')
                break

    #查看order
    def check_order(self):
        print('订单信息如下：')
        orders = order_all.keys()
        if len(orders) == 0:
            print('暂无订单')
        else:
            for order in orders:
                print('订单编号：', order_all[order].order_number, '房间号：', order_all[order].room_number, '入住时间：',
                      order_all[order].check_in_time, '离开时间：', order_all[order].check_out_time, '订单状态：',
                      order_all[order].order_status)


    # 预定房间
    def order_room(self):
        # 判断是否登陆
        if self.login():
            # 获取消费积分
            self.consumption = self.check_consumption()
            # 打印所有的房间种类和价格
            for i in room_all:
                for j in range(len(room_all[i])):
                    # 如果消费积分大于0
                    if self.consumption > 10:
                        # 打印房间种类和减去消费积分后的价格,10元封顶
                        print(f"{j}:{i} {room_all[i][j] - 10}")
                        # 消费积分减去10
                        self.consumption -= 10
                    else:
                        # 打印房间种类和价格
                        print(f"{j}:{i} {room_all[i][j]}")
            # 选择房间
            rent_time = input(input('请输入入住多少晚：'))
            if rent_time.isdigit():
                if rent_time == '0':
                    print('入住时间不能为0')
                    return False
                elif rent_time < '0':
                    print('入住时间不能为负数')
                    return False
                else:
                    rent_time = int(rent_time)
            room_num = int(input('请选择房间(编号)：'))
            #根据编号获取房间
            room_type = self.room_all[room_num]
            #根据房间种类随机生成房间号
            if room_num == 0:
                room_number = random.randint(100, 200)
            elif room_num == 1:
                room_number = random.randint(200, 300)
            elif room_num == 2:
                room_number = random.randint(300, 400)
            elif room_num == 3:
                room_number = random.randint(400, 500)
            # 判断房间是否存在
            if room_type in room_all:
                # 判断房间是否为空闲
                if room_all[room_type][room_num].room_status == '空闲':
                    # 判断消费积分是否大于0
                    if self.consumption > 10:
                        # 房间价格减去消费积分
                        room_all[room_type][room_num].room_price -= 10
                        # 消费积分减去10
                        self.consumption -= 10
                    # 房间状态改为已入住
                    room_all[room_type][room_num].room_status = '已入住'
                    # 房间入住时间
                    room_all[room_type][room_num].rent_time = rent_time

                    #根据时间生成订单号
                    order_number = time.strftime('%Y%m%d%H%M%S', time.localtime())
                    #生成订单
                    order_all[order_number] = {'order_number': order_number, 'room_number': room_number,
                                                  'room_type': room_type, 'room_price': room_all[room_type][room_num].room_price,
                                                    'rent_time': rent_time, 'waiter_name': self.waiter_name}
                    print('预定成功')
                    print('订单信息如下：')
                    print('订单号：', order_all[order_number]['order_number'], '房间号：', order_all[order_number]['room_number'],
                            '房间类型：', order_all[order_number]['room_type'], '房间价格：', order_all[order_number]['room_price'],
                            '入住时间：', order_all[order_number]['rent_time'])
                else:
                    print('该房间已被预定')

            # 判断是否已经被预定
            # if room_all[room_num][status] == '空闲':
                # # 根据房间号获取房间种类
                # room_all[room_num][status] = '预定'
                # room_all[room_num][rent_time] = rent_time
                # order_all[self.guest_name][order_room] = room_num
                # # order_all[self.guest_name][order_roomtype] = room_type暂未实现
                # order_all[self.guest_name][order_time] = rent_time
                # order_all[self.guest_name][order_service] = self.need_service
                # # 随机写入五位数的订单号
                # order_all[self.guest_name][order_id] = random.randint(10000, 99999)
                # # 添加到消费记录，房间号，入住天数，价格
                # consumption_all[self.guest_name][consumption].append(
                #     [room_num, rent_time, room_all[room_num][price]])

                print(f"预定成功，订单号为{order_all[self.guest_name][order_id]}")
            else:
                print('该房间已经被预定')

    #获取用户反馈
    def get_feedback(self):
        guest_name = input('请输入您的姓名：')
        feedback = input('请输入您的反馈：')
        #将反馈添加到字典中
        feedback_all[guest_name] = feedback
        print('反馈成功')

    #查看用户反馈
    def check_feedback(self):
        if len(feedback_all) == 0:
            print('暂无反馈')
        else:
            name = feedback_all.keys()
            for i in name:
                print(f'{i}:{feedback_all[i]}')
            print('\n    ')

    #取消预定
    def cancel_order(self):
        #输入订单号
        order_num = input('请输入订单号：')
        if order_num in order_all:
            #再次确认
            sure = input('是否确认取消该订单？(y/n)')
            if sure == 'y':
                #将订单状态改为取消
                order_all[order_num]['order_status'] = '取消'
                print('取消成功')
            else:
                print('取消取消')
        else:
            print('该订单不存在')

    #退房
    def check_out(self):
        #输入订单号
        order_num = input('请输入订单号：')
        if order_num in order_all:
            #再次确认
            sure = input('是否确认退房？(y/n)')
            if sure == 'y':
                #将订单状态改为退房
                order_all[order_num]['order_status'] = '退房'
                print('退房成功')
            else:
                print('取消退房')
        else:
            print('该订单不存在')

    #暂未实现
    #查看客户需要的services
    # def check_services(self):
    #     print('客户需要的服务如下：')
    #     for service in service_all:
    #         service.service_info()
    #         #将服务信息嵌套成字典
    #         service_info = {'service_name':service.service_name,'service_price':service.service_price}
    #         #将字典添加到列表中
    #         service_info.append(service_info)
    #
    #     return service_info


#客房管理员
class Room_manager:
    def __init__(self):
        self.name = None
        self.password = None

    #注册
    def register(self):
        name = input('请输入您的账号：')
        # 判断是否已经注册
        if name in room_manager_all:
            print('您已经注册过了')
            return False
        else:
            password = input('请输入您的密码：')
            # len()函数返回字典的长度
            num = len(room_manager_all) + 1
            room_manager_all[num] = {'name': name, 'password': password}
            print('注册成功')

    #登陆
    def login(self):
        name = input('请输入您的账号：')
        password = input('请输入您的密码：')
        count_manager = room_manager_all.keys()
        for i in count_manager:
            #判断是否注册过
            if name in room_manager_all[i]['name']:
                #判断密码是否正确
                if password == room_manager_all[i]['password']:
                    print('登陆成功')
                    return True
                else:
                    print('密码错误')
                    return False
            elif name not in room_manager_all[i]['name']:
                print('账号不存在')
                self.register()
                return False
            else:
                print('账号或密码错误')
                return False

    #查看房间信息
    def check_room(self):
        #调用waiter类的check_room方法
        Waiter().check_room()
        return False
    #修改房间状态
    def change_room(self):
        #获取房间信息
        room_info = Waiter().check_room()
        #输入房间号
        room_num = input('请输入房间号：')
        #判断房间号是否存在
        if room_num in room_info:
            #输入房间状态
            room_status = input('请输入房间状态：')
            #判断房间状态是否正确
            if room_status in ['空闲','预定','入住','维修']:
                #将房间状态修改
                room_info[room_num]['room_status'] = room_status
                print('修改成功')
            else:
                print('房间状态错误')




#客人
class Guest:
    #读取config文件中的guest_all
    def __init__(self):
        self.guest_name = None
        self.guest_password = None
        self.guest_phone = None
        self.service = None
        self.consumption_all = None
        self.id = None

    #注册
    def register(self):
        guest_name = input('请输入您的账号：')
        #判断是否已经注册
        if guest_name in guest_all:
            print('该用户已经注册')
            return False
        else:
            print('欢迎注册')
            name = input('请输入姓名：')
            password = input('请输入密码：')
            phone = input('请输入手机号：')
            #密码不为空
            if password != '':
                num = len(guest_all) + 1
                self.id = num
                guest_all[num] = {'guest_name': name, 'guest_password': password, 'guest_phone': phone,'consumption_all':[]}
                # print(guest_all)
                print('注册成功')
                return True


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
        # 再次确认
        sure = input('是否确认修改个人信息？(y/n)')
        if sure == 'y':
            password = input('请输入密码：')
            phone = input('请输入手机号：')
            # 修改
            self.guest_password = password
            self.guest_phone = phone
            print('修改成功')
        else:
            print('取消修改')



    #消费记录查询
    def check_consumption(self):
        #根据id获取消费记录
        consumption = guest_all[self.id]['consumption_all']
        #判断是否有消费记录
        if consumption == []:
            print('您还没有消费记录')
        else:
            print('您的消费记录为：')
            for i in consumption:
                print(i)

    #统计消费记录积累积分
    def count_score(self):
        #获取消费记录中的消费金额
        consumption = guest_all[self.id]['consumption_all']
        #判断是否有消费记录
        if consumption == []:
            print('您还没有消费记录')
        else:
            #积分
            score = 0
            for i in consumption:
                score += i['consumption_money']
            print('您的积分为：',score)
    #续订房间
    def renew_room(self):
        # 询问是否需要续订
        sure = input('是否需要续订？(y/n)')
        if sure == 'y':
            # # 如果需要，输入续订天数
            # rent_time = int(input('请输入续订天数：'))
            # # 根据积分减去房间价格打印出来
            # self.score = self.count_score()
            # # 如果积分大于10
            # if self.score > 10:
            #     # 打印房间种类和减去消费积分后的价格,10元封顶
            #     print('房间种类：{}，价格：{}'.format(room_all[room_num][room_type], room_all[room_num][price] - 10))
            #     # 消费积分减去10
            #     self.score -= 10
            # else:
            #     # 打印房间种类和价格
            #     print('房间种类：{}，价格：{}'.format(room_all[room_num][room_type], room_all[room_num][price]))
            #
            # # 修改rent_time
            # for i in order_all[self.guest_name]:
            #     room_all[i][rent_time] += rent_time
            #     # 修改根据id修改消费记录
            #     guest_all[self.id]['consumption_all'].append(['续订', room_all[i][room_type], room_all[i][price] * rent_time])
            print('续订成功')
        else:
            print('取消续订')


    #入住需求的服务
    def need_service(self):
        self.services = ["早餐送到房间(30元)","代烫衣服(20元)"]
        self.services_price = [30,20]
        sure = input('是否需要服务？(y/n)')
        if sure == 'y':
            for i in enumerate(self.services):
                print(f"{i[0]} {i[1]}")
            # 选择服务
            service_num = int(input('请选择服务(编号)：'))
            # 根据id添加消费金额
            guest_all[self.id]['consumption_all'].append([self.services_price[service_num]])
            # 写入房间号和服务到order_all
            order_all[self.guest_name][order_service].append(
                [order_all[self.guest_name][order_room][-1], self.services[service_num]])
            print('服务成功')
        else:
            print('取消服务')



    #跟前台反应需求
    def need_feedback(self):
        # 输入反馈
        feedback = input('请输入反馈：')
        # 写入反馈到feedback_all
        feedback_all[self.guest_name] = feedback
        print('反馈成功')


#主循环
while True:
    #打印欢迎界面
    print('欢迎使用酒店管理系统')
    #选择经理、前台服务员、客房管理员、客户会员、退出
    print('1.经理\n2.前台服务员\n3.客房管理员\n4.客户会员\n5.退出')
    try:
        # 输入选择
        choice = int(input('请选择：'))
    except:
        print('输入错误\n    ')
        continue
    #判断选择
    if choice == 1:
        #经理
        manager = Manager()
        ok = manager.login()
        if ok == True:
            # 登陆成功后，选择功能
            while True:
                print('1.雇佣员工\n2.解雇员工\n3.查看员工信息\n4.退出')
                choice = int(input('请选择：'))
                if choice == 1:
                    manager.hire()
                elif choice == 2:
                    manager.fire()
                elif choice == 3:
                    manager.check_waiter()
                elif choice == 4:
                    break
        elif ok == False:
            break
    elif choice == 2:
        #前台服务员
        waiter = Waiter()
        ok = waiter.login()
        #如果login（）返回True
        if ok == True:
            # 登陆成功后，选择功能
            while True:
                print('1.查看房间\n2.查看订单\n3.查看消费记录\n4.查看反馈\n5.记录用户反馈\n6.退出')
                choice = int(input('请选择：'))
                if choice == 1:
                    waiter.check_room()
                elif choice == 2:
                    waiter.check_order()
                elif choice == 3:
                    waiter.check_consumption()
                elif choice == 4:
                    waiter.check_feedback()
                elif choice == 5:
                    waiter.get_feedback()
                elif choice == 6:
                    break

        elif waiter.login() == False:
            print('登陆失败')

    elif choice == 3:
        #客房管理员
        room_manager= Room_manager()
        room_manager.login()
        #打印功能
        while True:
            #查看房间状态
            print('1.查看房间状态\n2.修改房间状态\n3.退出')
            choice = int(input('请选择：'))
            if choice == 1:
                room_manager.check_room()
            elif choice == 2:
                room_manager.change_room()
            elif choice == 3:
                break
    elif choice == 4:
        #客户会员
        guest = Guest()
        ok = guest.register()
        if ok == False:
            break
        #登陆成功后，选择功能
        while True:
            print('1.修改个人信息\n2.消费记录查询\n3.需求的服务\n4.反馈\n5.续订\n6.退出')
            choice = int(input('请选择：'))
            if choice == 1:
                guest.change_info()
            elif choice == 2:
                guest.check_consumption()
            elif choice == 3:
                guest.need_service()
            elif choice == 4:
                guest.need_feedback()
            elif choice == 5:
                guest.renew_room()
            elif choice == 6:
                break








