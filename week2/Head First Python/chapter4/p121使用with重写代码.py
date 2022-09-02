# @Time: 2022/9/1 19:38
# @Author: 李树斌
# @File : p121使用with重写代码.py
# @Software :PyCharm
import nesterbing

try:
    with open("data_man.txt",'w') as data_man:
        nesterbing.print_lol(man,fh=data_man)
    with open("data_other.txt",'w') as data_other:
        nesterbing.print_lol(other,fh=data_other)
except IOError as err:
    print("File:" + str(err))