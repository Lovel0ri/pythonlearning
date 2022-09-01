# @Time: 2022/9/1 15:23
# @Author: 李树斌
# @File : 以写模式打开文件.py
# @Software :PyCharm

out = open("data.out","w")
print("hello,Bingbing",file=out)
out.close()