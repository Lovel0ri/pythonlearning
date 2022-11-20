# @Time: 2022/11/20 14:58
# @Author: 李树斌
# @File : 使用UserDict.py
# @Software :PyCharm
from collections import UserDict
#查看UserDict的属性和方法
# print(dir(UserDict))
#查看UserDict的帮助文档
#print(help(UserDict))

class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item