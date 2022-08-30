# @Time : 2022/8/29  17:57
# @Author: 李树斌
# @File : demo1.py
# @Software : PyCharm

#%方式
age = 20
country = "中国"
# print("我的年龄是%d岁"%age)
# print("我的国籍是%s"%country)
# print("我的年龄是%d岁,我的国籍是%s"%(age,country))

#format()函数
#1.顺序填充
str="我的名字是{},我的年龄是{},我的国籍是{}".format("李树斌",20,"中国")
print(str)

#2.索引填充
str="我的名字是{1},我的年龄是{2},我的国籍是{0}".format("中国","李树斌",20)
print(str)

#3.关键字填充
str="姓名:{name},年龄:{age}".format(name = "李树斌", age = 20)
print(str)

#4.通过字典设置参数，**展开map集合
info = {"name":"张三","age": 18}
str = "姓名:{name},年龄:{age}".format(**info)
print(str)

#5.通过列表的索引设置参数
list = ["李树斌","冰冰","网络与新媒体"]
str = "姓名:{0[0]}, 外号:{0[1]},专业:{0[2]},方向:{1}".format(list,"数据科学与应用开发")
print(str)

#.2f打印2两位的浮点数
print("圆周率:{:.2f}".format(3.1415926))
#.3f打印3位的浮点数
print("圆周率:{:.3f}".format(3.1415926))

print("{:.1%}".format(0.25))

str = "python学习"
print("{:*>10}".format(str))
print("{:*<10}".format(str))
print(("{:#^10}".format(str)))