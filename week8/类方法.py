# @Time: 2022/10/15 12:29
# @Author: 李树斌
# @File : 类方法.py
# @Software :PyCharm
class CLanguage:
    # 类构造方法，也属于实例方法
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"

    # 下面定义了一个类方法
    @classmethod
    def info(cls):
        print("正在调用类方法", cls)


# 使用类名直接调用类方法(推荐)
CLanguage.info()
# 使用类对象调用类方法
clang = CLanguage()
clang.info()