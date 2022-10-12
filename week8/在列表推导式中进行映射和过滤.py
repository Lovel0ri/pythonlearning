# @Time: 2022/10/12 22:51
# @Author: 李树斌
# @File : 在列表推导式中进行映射和过滤.py
# @Software :PyCharm
mapObj = map(lambda n: str(n),[1,2,3,4,5])
print(list(mapObj))
print([str(n) for n in [1,2,3,4,5]])

filterObj = filter(lambda n : n % 2 ==0 , [1,2,3,4,5,6,7,8])
print(list(filterObj))