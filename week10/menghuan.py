# @Time: 2022/10/26 13:59
# @Author: 李树斌
# @File : menghuan.py
# @Software :PyCharm
from ctypes import CDLL
from datetime import time
dll_path = 'E:\\网络与新媒体\\github\pythonlearning\\week10\\kmclassdll-x64\\kmclassdll.dll'#dll文件的路径
driver_path = 'kmclass-x64\\kmclass\\kmclass.sys'#驱动文件的路径

#加载dll文件
dll = CDLL(dll_path)
#加载驱动
dll.KMClassLoadDriver(driver_path)
#启动驱动
dll.KMClassStartDriver()
#设置梦幻西游的文件路径
dll.KMClassSetPath('E:\\网络与新媒体\\爬虫\\梦幻西游\\my.exe')
#启动游戏
dll.KMClassStartGame()



