# @Time: 2022/9/1 19:38
# @Author: 李树斌
# @File : p121使用with重写代码.py
# @Software :PyCharm

try:
    with open("data_man.txt",'w') as data_man:
        print(man,file=data_man)
    with open("data_other.txt",'w') as data_other:
        print(other,file=data_other)
except IOError as err:
    print("File:" + str(err))