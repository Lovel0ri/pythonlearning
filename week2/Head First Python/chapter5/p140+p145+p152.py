# @Time: 2022/9/3 13:55
# @Author: 李树斌
# @File : p140+p145+p152.py
# @Software :PyCharm
from sanitizeb import sanitizeb

import nesterbing
# def sanitize(time_string):
#     if '-' in time_string:
#         splitter = '-'
#     elif '.' in time_string:
#         splitter = '.'
#     else:
#         return (time_string)
#     (mins, secs) = time_string.split(splitter)
#     return (mins + ':' + secs)

with open("hfpy_ch5_data/james.txt") as jaf:
    data = jaf.readline()
    james=data.strip().split(',')#split() 通过指定分隔符对字符串进行切片
with open("hfpy_ch5_data/julie.txt") as juf:
    data = juf.readline()
    julie=data.strip().split(',')
with open("hfpy_ch5_data/mikey.txt") as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
with open("hfpy_ch5_data/sarah.txt") as saf:
    data = saf.readline()
    sarah = data.strip().split(',')
# jamesp =sorted(james)
# juliep =sorted(julie)
# mikeyp =sorted(mikey)
# sarahp =sorted(sarah)

clean_james =sorted([sanitizeb(t) for t in james])
clean_julie = sorted([sanitizeb(t) for t in julie])
clean_mikey = sorted([sanitizeb(t) for t in mikey])
clean_sarah = sorted([sanitizeb(t) for t in sarah])

# for each_t in james:
#     clean_james.append(sanitizeb.sanitizeb(each_t))
# for each_t in julie:
#     clean_julie.append(sanitizeb.sanitizeb(each_t))
# for each_t in mikey:
#     clean_mikey.append(sanitizeb.sanitizeb(each_t))
# for each_t in sarah:
#     clean_sarah.append(sanitizeb.sanitizeb(each_t))
print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)