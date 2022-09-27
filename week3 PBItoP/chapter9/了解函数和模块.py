# @Time: 2022/9/28 1:52
# @Author: 李树斌
# @File : 了解函数和模块.py
# @Software :PyCharm
def greet_user(username):    #定义一个函数,关键词为"def",函数名为"greet_user",最后以“：”结尾
    """显示简单的问候语"""    #描述函数的具体功能
    print("Hello! {} {}".format(username,'!'))         #函数体的代码块，用于实现函数功能

greet_user("bingbing")         #调用函数