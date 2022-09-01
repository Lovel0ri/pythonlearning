# @Time: 2022/9/1 14:05
# @Author: 李树斌
# @File : try and except.py
# @Software :PyCharm

#打开文件并赋值到data,输出单个数据行
data = open('sketch.txt')
# print(data.readline(),end='')
# print(data.readline(),end='')

data.seek(0)
for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':', 1)  # 用split赋值到role和line_spoken
        print(role, end='')  # end=' '意思是末尾不换行，加空格
        print(" said:", end='')
        print(line_spoken, end='')
    except:
        pass

data.close()
