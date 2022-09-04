# @Time: 2022/9/4 1:00
# @Author: 李树斌
# @File : p175字典处理数据.py
# @Software :PyCharm
# class Athlete:
#     def __init__(self, a_name, a_dob=None, a_times=[]):
#         self.name = a_name
#         self.dob = a_dob
#         self.times = a_times
#     def top3 (self):
#         return(sorted(set([sanitizeb(t) for t in self.times]))[0:3])
#
#     def add_time(self,time_value):
#         self.times.append(time_value)
#     def add_times(self,list_of_times):
#         self.times.extend(list_of_times)
#



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
            temple = data.strip().split(',')
            return (
                AthleteList(temple.pop(0),temple.pop(0),temple)
            )
    except IOError as ioerr:
        print("File error" + str(ioerr))
        return (None)

class AthleteList(list):
    def __init__(self, a_name, a_dob= None, a_times=None):
        list.__init__([])
        if a_times is None:
            a_times = []
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitizeb(t) for t in self]))[0:3])

sarah = get_coach_data("hfpy_ch6_data/sarah2.txt")
james = get_coach_data("hfpy_ch6_data/james2.txt")
mikey = get_coach_data('hfpy_ch6_data/mikey2.txt')
julie = get_coach_data('hfpy_ch6_data/julie2.txt')

# vera = AthleteList('Vera Vi')
# vera.append('1.31')
# print(vera.top3())
# vera.extend(['2.22','1-21','2:22'])
# print(vera.top3())
# (sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
# #唯一可下标的内置函数：
# # string:  "foobar"[3] == "b"
# # tuple:   (1,2,3,4)[3] == 4
# # list:    [1,2,3,4][3] == 4
# # dict:    {"a":1, "b":2, "c":3}["c"] == 3
# print(sarah_name + "'s fastest times are :" + str(sorted(set([sanitizeb(t) for t in sarah]))[0:3]))
#
# sarah_data = {}
# sarah_data['Name'] = sarah.pop(0)
# sarah_data['DOB'] = sarah.pop(0)
# sarah_data['Time'] = sarah
print(sarah.name + "'s fastest times are :" + str(sarah.top3()))
print(james.name + "'s fastest times are :" + str(james.top3()))
print(mikey.name + "'s fastest times are :" + str(mikey.top3()))
print(julie.name + "'s fastest times are :" + str(julie.top3()))