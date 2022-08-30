#判断今天星期几，星期二的话打印python课表
import time
today = time.localtime().tmday
if today == 1:
	print("今天是星期二有python课，时间是2.30到4.50")
else:
	print("今天没有python课")

