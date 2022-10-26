# @Time: 2022/10/26 12:18
# @Author: 李树斌
# @File : maxnum.py
# @Software :PyCharm

#同时获取用户输入的三个数字赋值到变量a、b、c中
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = int(input("请输入第三个数字："))

#b,c

#三个数字比大小
if a > b:      #a > b ,a > c
    if a > c:
        print("最大值为：",a)#a > b > c
    else:
        print("最大值为：",c)#c >= a,  a > b
else:#a < b
    if b > c:
        print("最大值为：",b)
    else:#b <= c
        print("最大值为：",c)


