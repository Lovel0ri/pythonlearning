# @Time: 2022/9/3 16:08
# @Author: 李树斌
# @File : p156列表推导例子练习.py
# @Software :PyCharm
from sanitizeb import sanitizeb


# mins = [1,2,3]
# secs = [m*60 for m in mins]
# print(secs)
# meters = [1,2,3]
# feet = [m*3.281 for m in meters]
# print(feet)
#
# lower = ["I","don't","like","spam"]
# upper = [s.upper() for s in lower]
# print(upper)

dirty = ['2-22','2:22','2.22']
clean = [float(s) for s in dirty]
# clean = [float(sanitizeb(t)) for t in ['2-22','2.22','2:22']]

print(clean)


