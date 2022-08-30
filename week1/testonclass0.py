#head firsd阿松sadsadasdasdast python P4
import datetime
#本项目用到了时间模块
print(datetime.datetime.today().microsecond)
odds = [ 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
right_this_minute = datetime.datetime.today().minute

if right_this_minute in odds:
	print("This minute seems a little odd.")
else:
	print("Not an odd minute.")
print(datetime.datetime.today().microsecond)
