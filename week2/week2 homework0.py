# @Time : 2022/8/30  18:31
# @Author: 李树斌
# @File : week2 homework0.py
# @Software : PyCharm
# import time
# #设置好上下课时间
# time_shangkehour = 14
# time_shangkemin = 30
# time_xiakehour = 16
# time_xiakemin = 50
# timehour = int(time.strftime('%H'))
# timemin = int(time.strftime('%M'))
# days = {'星期一','星期二','星期三','星期四','星期五',"星期六",'星期天'}
# # 获取时间
# # print(localtime)
# today = time.localtime().tm_wday
# if today == 1:
#     print(f"今天是星期{today+1}有python课，时间是2.30到4.50")
#     print(f"现在是{time.strftime('%H:%M', time.localtime(time.time()))}")
#     if timehour <= time_shangkehour:
#         print("还没开始上课哈哈")
#     else:
#     # 判断现在时间是否是2点
#         if timehour == time_shangkehour:
#         # 判断现在时间是否是2：30之前
#             if timemin <= time_shangkemin:
#                 print("还有半小时不到就要上课咯")
#             else:
#                 print("开始上课啦")
#         # 判断现在时间是否是4：50之前
#         elif timehour == time_xiakehour and timemin <= time_xiakemin:
#             print("专心上课")
#         else:
#             print("下课啦")
# else:
# 	print("今天没有python课")

import time
time_shangkehour,time_shangkemin,time_xiakehour,time_xiakemin  = 14,30,16,50
timehour,timemin = int(time.strftime('%H')),int(time.strftime('%M'))
days = {'星期一':0,'星期二':1,'星期三':2,'星期四':3,'星期五':4,"星期六":5,'星期天':6}
today = time.localtime().tm_wday#获取今天星期几
if today == 1:
    print(f"今天是星期二有python课，时间是2.30到4.50\n现在是{time.strftime('%H:%M', time.localtime(time.time()))}")
    if timehour < time_shangkehour:#是否小于2点
        print("还没开始上课哈哈")
    elif timehour == time_shangkehour and timemin <= time_shangkemin:#是否早于2：30
            print("就要上课咯")
    elif timehour <= time_xiakehour:
            print("专心上课")
    elif timehour == time_xiakehour and timemin <= time_shangkemin:
            print("专心下课")
    else:
        print("下课啦")
else:
    print("今天没有python课")

# 使用 strptime() 方法，通过传递包含日期和时间的字符串，得到一个 datetime 对象。
# 然后我们可以通过 .hour 和 .minute 属性从 datetime 对象中得到小时和分钟。
# time = datetime.strptime("30/08/22 16:30", "%d/%m/%y %H:%M")
# time = time.strftime('%H:%M:%S',time.localtimeint(time.time()))

# print(f"现在是{datetime.hour}:{datetime.minute}")




