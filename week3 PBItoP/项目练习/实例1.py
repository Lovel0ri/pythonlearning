# @Time: 2022/9/13 18:20
# @Author: 李树斌
# @File : 实例1.py
# @Software :PyCharm

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if  i != j and i != k and j != k:
                print(i,j,k)