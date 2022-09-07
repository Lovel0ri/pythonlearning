# @Time: 2022/9/4 21:42
# @Author: 李树斌
# @File : Homework plus.py
# @Software :PyCharm
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
#week2 作业改进版
# import time
# time_shangkehour,time_shangkemin,time_xiakehour,time_xiakemin  = 14,30,16,50
# timehour,timemin = int(time.strftime('%H')),int(time.strftime('%M'))
# days = {'星期一':0,'星期二':1,'星期三':2,'星期四':3,'星期五':4,"星期六":5,'星期天':6}
# today = time.localtime().tm_wday#获取今天星期几
# if today == 6:
#     print("今天是星期二有python课，时间是2.30到4.50")
#     print(f"现在是{time.strftime('%H:%M', time.localtime(time.time()))}")
#     if timehour < time_shangkehour:#是否小于2点
#         print("还没开始上课哈哈")
#     elif timehour == time_shangkehour and timemin <= time_shangkemin:#是否早于2：30
#             print("就要上课咯")
#     elif timehour <= time_xiakehour:
#             print("专心上课")
#     elif timehour >time_xiakehour or timehour == time_xiakehour and timemin >= time_xiakemin:
#             print("下课啦")
# else:
#     print("今天没有python课")
#  16>16 or 16 == 16 and 50 >= 50
# 2:30 - 4:50

# 18:20

