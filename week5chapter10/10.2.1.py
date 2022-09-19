# @Time: 2022/9/19 22:14
# @Author: 李树斌
# @File : 10.2.1.py
# @Software :PyCharm

filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write('I love Python,too.\n')
    file_object.write('I love Python,too.\n')