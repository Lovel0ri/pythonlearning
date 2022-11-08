# @Time: 2022/11/6 14:13
# @Author: 李树斌
# @File : 使用ConfigParser的程序.py
# @Software :PyCharm
from configparser import ConfigParser

CONFIGFILE ='area.ini'

#创建一个ConfigParser对象
config = ConfigParser()
#读取配置文件
config.read(CONFIGFILE)

#打印问候语
print(config.get('messages','greeting'))