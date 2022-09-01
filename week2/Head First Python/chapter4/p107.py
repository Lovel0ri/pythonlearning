# @Time: 2022/9/1 14:41
# @Author: 李树斌
# @File : p107.py
# @Software :PyCharm

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
print(man)
print(other)