# @Time: 2022/9/3 22:24
# @Author: 李树斌
# @File : get_coach_data.py
# @Software :PyCharm

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return (data.strip().split(','))
    except IOError as ioerr:
        print("File error" + str(ioerr))
        return (None)
