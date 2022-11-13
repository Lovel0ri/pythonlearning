# @Time: 2022/11/9 17:59
# @Author: 李树斌
# @File : 内存视图.py
# @Software :PyCharm
import array
# array.array() 用于创建数组
numbers = array.array('h',[-2,-1,0,1,2])
# memoryview() 用于创建内存视图
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

#把内存视图的内容转换成字节序列（bytes）
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 2
print(numbers)