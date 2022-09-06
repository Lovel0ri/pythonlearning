# @Time: 2022/9/6 17:29
# @Author: 李树斌
# @File : p4.3.2.py
# @Software :PyCharm
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))

squares = [value**2 for value in range(1,11)]
print(squares)