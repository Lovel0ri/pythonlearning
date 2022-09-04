# @Time: 2022/9/4 1:00
# @Author: 李树斌
# @File : p175字典处理数据.py
# @Software :PyCharm

def sanitizeb(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+'.'+secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return (data.strip().split(','))
    except IOError as ioerr:
        print("File error" + str(ioerr))
        return (None)


sarah = get_coach_data("hfpy_ch6_data/sarah2.txt")
# (sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
# #唯一可下标的内置函数：
# # string:  "foobar"[3] == "b"
# # tuple:   (1,2,3,4)[3] == 4
# # list:    [1,2,3,4][3] == 4
# # dict:    {"a":1, "b":2, "c":3}["c"] == 3
# print(sarah_name + "'s fastest times are :" + str(sorted(set([sanitizeb(t) for t in sarah]))[0:3]))

sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Time'] = sarah
print(sarah_data['Name'] + "'s fastest times are :" + str(sorted(set([sanitizeb(t) for t in sarah_data['Time'] ]))[0:3]))