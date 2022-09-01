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
# print(man)
# print(other)
try:
    data_man = open("data_man","w")
    data_other = open("data_other","w")

    #把台词分别输出到两个data文件
    print(man,file=data_man)
    print(other,file=data_other)

    # data_man.close()#如果上面两个输出有一个出错，这两个文件就无法关闭，可能导致数据丢失被破坏
    # data_other.close()
except IOError:
    print('File error')

#如果没有出现任何运行时的错误，会执行finall组中的代码。如果出现IOerror，会执行except组，然后运行finally组。
#无论如何都要关闭文件
finally:
    data_man.close()
    data_other.close()
