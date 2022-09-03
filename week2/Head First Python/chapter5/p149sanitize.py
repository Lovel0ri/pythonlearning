# @Time: 2022/9/3 14:55
# @Author: 李树斌
# @File : p149sanitize.py
# @Software :PyCharm

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+'.'+secs)