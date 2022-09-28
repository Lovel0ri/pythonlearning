# @Time: 2022/9/28 1:52
# @Author: 李树斌
# @File : 了解函数和模块.py
# @Software :PyCharm
"""def greet_user(username):  # 定义一个函数,关键词为"def",函数名为"greet_user",最后以“：”结尾
     显示简单的问候语 # 描述函数的具体功能
    print("Hello! {} {}".format(username, "!"))  # 函数体的代码块，用于实现函数功能


greet_user("bingbing")  # 调用函数"""

"""2.2 实参和形参
greet_user(username) #username 为形参；函数完成其工作时所需要的信息。

greet_user("zhichao") #"zhichao"为实参；实参是调用函数时传递给函数的信息。

形参：形式参数，不是实际存在的，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参

实参：实际参数，调用函数时传递给函数的参数，可以是常量、变量，表达式，函数，传给形参

区别：形参是虚拟的，不占用空间，形参变量只有在被调用时才分配内存单元，实参是一个变量，占用内存空间，数据传递单向，实参传给形参，不能倒过来。"""


"""def func_test(x, y, z):
    print(x)
    print(y)


func_test(1, y=2, 3)"""

#SyntaxError: positional argument follows keyword argument
#关键字参数必须跟随在位置参数后面
def func_test(x, y, z):
    print(x)
    print(y)


func_test(1, 3,y=2)
#ypeError: func_test() got multiple values for argument 'y'

返回值是字典，而我们要取字典中的某个值时：

def func1():
    parameters = {'a': 1, 'b': 2, 'c': 3}
    return parameters


def func1():
    parameters = {'a': 1, 'b': 2, 'c': 3}
    return parameters


"""func1().get('a')
输出：1

返回值是列表，而我们要取列表中的某个值时：


def func2():
    parameters = [1,2,3]
    return parameters

func2()[1]
输出：2

总结：直接将函数
func()
当作某个字典或列表的名字，使用字典查询或列表索引的方式取值即可"""