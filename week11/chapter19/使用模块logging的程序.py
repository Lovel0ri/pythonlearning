# @Time: 2022/11/6 14:30
# @Author: 李树斌
# @File : 使用模块logging的程序.py
# @Software :PyCharm
import logging
logging.basicConfig(level=logging.INFO,filename='mylog.log')
logging.info('Start of program')

logging.info('trying to divide 1 by 0')
print(1/0)

logging.info('The division succeeded')
logging.info('End of program')