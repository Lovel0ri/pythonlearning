# @Time: 2022/10/16 16:48
# @Author: 李树斌
# @File : flatten.py
# @Software :PyCharm
def flatten(nested):
    try:
        # 不迭代类似于字符串的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

# print(list(flatten([[1,2],3])))
# print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flatten([['nihao'],[2,3],1])))
print(type([['nihao'],[2,3],1]))
