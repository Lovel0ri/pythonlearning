# @Time: 2022/9/1 12:06
# @Author: 李树斌
# @File : sketch.py
# @Software :PyCharm
import os
os.chdir('../chapter3')
#查看工作目录是否正确
print(os.getcwd())

#打开文件并赋值到data,输出单个数据行
data = open('sketch.txt')
# print(data.readline(),end='')
# print(data.readline(),end='')

data.seek(0)
if os.path.exists('sketch.txt'):
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)  # 用split赋值到role和line_spoken
            print(role, end='')  # end=' '意思是末尾不换行，加空格
            print(" said:", end='')
            print(line_spoken, end='')
else:
    print('这个文件已经被删除')
data.close()
