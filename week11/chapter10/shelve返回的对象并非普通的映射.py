# @Time: 2022/11/1 23:28
# @Author: 李树斌
# @File : shelve返回的对象并非普通的映射.py
# @Software :PyCharm
import shelve
s = shelve.open("test.dat")
s["x"] = ["a", "b", "c"]
s["x"].append("d")
print(s["x"])
#将获取的副本赋给一个变量，然后对这个变量进行操作
temp = s["x"]
temp.append("e")
print(s["x"])
print(temp)
print('')
#操作完毕后，将副本重新赋值给原来的变量
s["x"] = temp
print(s["x"])