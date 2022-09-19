# @Time: 2022/9/20 0:46
# @Author: 李树斌
# @File : test0.py
# @Software :PyCharm
try:
    n = int(input("请输入整数："))
    if n != 1 and type(n) == int and n > 1:
        for i in range(2, n):
            b = n % i
            if b == 0:
                print("不是素数")
                break
        else:
            print("是素数")
    elif n == 1:
        print("1不是素数")
    else:
        print("请输入正确的正整数")
except ValueError:
    print("请输入正确的正整数")