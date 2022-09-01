# @Time: 2022/9/1 18:52
# @Author: 李树斌
# @File : missing.py
# @Software :PyCharm

try:
    data = open("missing.txt")
    print(data.readline(),end='')
except IOError as err:
    print("File error:" + str(err))
finally:
    if "data" in locals():
        data.close()
