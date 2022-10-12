# @Time: 2022/10/12 22:27
# @Author: 李树斌
# @File : lambda.py
# @Software :PyCharm

#lambda函数也被称为匿名函数或者无名函数
# def rectanglePerimeter(rect):
#     return (rect[0] * 2) + (rect[1] * 2)


rectanglePerimeter = lambda rect:(rect[0] * 2) + (rect[1] * 2)
print(rectanglePerimeter([4,10]))