# @Time: 2022/9/3 13:55
# @Author: 李树斌
# @File : p140+p145+p152.py
# @Software :PyCharm
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + ':' + secs)

with open("hfpy_ch5_data/james.txt") as jaf:
    data = jaf.readline()
    james=data.strip().split(',')
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

clean_james =[]
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))
print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)