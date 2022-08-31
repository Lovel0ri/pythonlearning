# @Time : 2022/8/31  13:19
# @Author: 李树斌
# @File : 含有return的递归函数.py
# @Software : PyCharm

# def jie_cheng(n):
#     if n <= 1:
#         return 1
#     return n * jie_cheng(n - 1)


# print(jie_cheng(3))


def get_num(num):
    if num > 2:
        get_num(num - 1)
    print(num)

get_num(3)#输出结果 2 3 4

def get_num(num):
    if num > 2:
        get_num(num - 1)
    else:
        print(num)


get_num(4) # 输出结果为 2
'''
解析一下：加了else后，首先代码区有两个分支，
在num>2时，执行会有递归，当n=4 是开辟一层空间；
n=3时开辟一层空间，此时 get_num(2) 再开辟一个空间，
当它从上往下执行过程中，在他本层空间遇到if num>2 不成立，所以走分支 else，直接打印出来；
此时代码还没结束，回到上一层空间，num=3, num>2 已经进入了if 不会走else，
num=4 也不会走else，所以这两层空间没有值输出！
'''
"""版权声明：本文为CSDN博主「storyfull」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/storyfull/article/details/102671946"""

