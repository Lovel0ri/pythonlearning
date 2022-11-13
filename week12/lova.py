# @Time: 2022/11/13 1:14
# @Author: 李树斌
# @File : lova.py
# @Software :PyCharm


#画一个动态的爱心
import turtle
import time


#动态渲染的粒子爱心
def love():
    turtle.pensize(5)
    turtle.pencolor('red')
    turtle.fillcolor('pink')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(150)
    turtle.circle(-90, 180)
    turtle.left(90)
    turtle.circle(-90, 180)
    turtle.forward(150)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    love()

