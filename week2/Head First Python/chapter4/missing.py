# @Time: 2022/9/1 18:52
# @Author: 李树斌
# @File : missing.py
# @Software :PyCharm

# try:
#     data = open("missing.txt",'w')
#     print(data.readline(),end='')
# except IOError as err:
#     print("File error:" + str(err))
# finally:
#     if "data" in locals():
#         data.close()


# 使用with减少额外代码
try:
    with open("missing.txt",'w') as data:
        print("it's a test3.",file=data)
except IOError as err:
    print("File error" + str(err))
