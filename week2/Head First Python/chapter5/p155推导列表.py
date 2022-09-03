# @Time: 2022/9/3 15:53
# @Author: 李树斌
# @File : p155推导列表.py
# @Software :PyCharm

"""

clean_mikey = []#1.创建
for each_t in mikey: #2.迭代
    clean_mikey.append(sanitize(each_t))#3.转换
                #4.追加
""""
#使用列表推导
#clean_mikey = [p149sanitize.sanitize(each_t) for each_t in mikey]