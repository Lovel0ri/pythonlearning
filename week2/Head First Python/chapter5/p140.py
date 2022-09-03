# @Time: 2022/9/3 13:55
# @Author: 李树斌
# @File : p140.py
# @Software :PyCharm

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

print(james)
print(julie)
print(mikey)
print(sarah)