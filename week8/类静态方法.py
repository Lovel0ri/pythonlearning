# @Time: 2022/10/15 13:23
# @Author: 李树斌
# @File : 类静态方法.py
# @Software :PyCharm
class CLanguage:
    @staticmethod
    def info(name,add):
        print(name,add)

#使用类名直接调用静态方法
print(CLanguage.info("冰冰","21网新"))
#使用类对象调用静态方法
clang = CLanguage()
print(clang.info("冰冰","21网新"))