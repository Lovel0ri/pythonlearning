# @Time: 2022/9/1 14:41
# @Author: 李树斌
# @File : p107+with重写代码+异常处理+pickle.py
# @Software :PyCharm
import pickle

import nesterbing
#import本地的模块报错解决办法 https://blog.csdn.net/gaoqing_dream163/article/details/109219452
#https://blog.csdn.net/m0_51711485/article/details/124119651?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166207906016782412546982%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=166207906016782412546982&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-124119651-null-null.142^v44^new_blog_pos_by_title&utm_term=pycharm%E4%BF%AE%E6%94%B9%E5%BC%95%E5%85%A5%E6%A8%A1%E5%9D%97%E7%9A%84%E8%B7%AF%E5%BE%84&spm=1018.2226.3001.4187
# import sys
# sys.path.append("")


man = []
other = []

try:
    data = open('../chapter3/sketch.txt')
    # print(data.readline(),end='')
    # print(data.readline(),end='')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)  # 用split赋值到role和line_spoken
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)



        except ValueError:
            pass

    data.close()
except IOError:
    print("这个文件不存在")

#使用with重写try\except代码减少额外代码
try:
    with open("data_man.txt",'wb') as data_man, open("data_other.txt",'wb') as data_other:
        pickle.dump(man,data_man)
        pickle.dump(other,data_other)
    with open("data_man.txt","rb") as restoredata_man,open("data_other.txt","rb") as restoredata_other:
        data_man_list = pickle.load(restoredata_man)
        data_other_list = pickle.load(restoredata_other)
    print(data_man_list)
    print(data_other_list)


except IOError as err:
    print("File:" + str(err))
except pickle.PickleError as prr:
    print("Pickle error"+str(prr))
# print(man)
# print(other)
# try:
#     data_man = open("data_man.txt", "w")
#     data_other = open("data_other.txt", "w")
#
#     #把台词分别输出到两个data文件
#     print(man,file=data_man)
#     print(other,file=data_other)
#
#     # data_man.txt.close()#如果上面两个输出有一个出错，这两个文件就无法关闭，可能导致数据丢失被破坏
#     # data_other.txt.close()
# except IOError:
#     print('File error')
#
# #如果没有出现任何运行时的错误，会执行finally组中的代码。如果出现IOerror，会执行except组，然后运行finally组。
# #无论如何都要关闭文件
# finally:
#     data_man.close()
#     data_other.close()

