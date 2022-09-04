# @Time: 2022/9/4 11:48
# @Author: 李树斌
# @File : p194创建类Athlete.py
# @Software :PyCharm

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

sarah = Athlete('Sarah Sweeney','2002-6-17', ['2:58','2.58','1.56'])
james = Athlete('James Jones')
print(sarah)
print(james)