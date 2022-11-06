# @Time: 2022/11/4 21:12
# @Author: 李树斌
# @File : 16-1测试程序.py
# @Software :PyCharm
from area import react_area


height = 3
width = 4
correct = 12
answer = react_area(height, width)
if answer == correct:
    print('Correct!')
else:
    print('Incorrect!')