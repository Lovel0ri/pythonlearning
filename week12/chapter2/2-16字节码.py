# @Time: 2022/11/9 14:41
# @Author: 李树斌
# @File : 2-16字节码.py
# @Software :PyCharm
import dis

dis.dis('s[a] += b')
#  1           0 LOAD_NAME                 0 (s)
#              2 LOAD_NAME                1 (a)
#              4 DUP_TOP_TWO# 重复栈顶两个元素
#              6 BINARY_SUBSCR # 从栈顶弹出两个元素，第一个元素是序列，第二个元素是索引，然后从序列中取出索引对应的元素，放到栈顶
#              8 LOAD_NAME                2 (b)
#             10 INPLACE_ADD # 从栈顶弹出两个元素，第一个元素是可变序列，第二个元素是要添加的元素，然后将元素添加到可变序列中
#             12 ROT_THREE# 旋转栈顶三个元素
#             14 STORE_SUBSCR           3   0   赋值失败
#             16 LOAD_CONST               0 (None)
#             18 RETURN_VALUE