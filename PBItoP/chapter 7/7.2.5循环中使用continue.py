# @Time: 2022/9/6 20:19
# @Author: 李树斌
# @File : 7.2.5循环中使用continue.py
# @Software :PyCharm

current_number = 0
while current_number <= 10:
    print(current_number)
    current_number+=1
    if current_number %2 == 0:
        continue
print(current_number)