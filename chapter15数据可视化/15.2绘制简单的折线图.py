# @Time: 2022/9/25 22:31
# @Author: 李树斌
# @File : 15.2绘制简单的折线图.py
# @Software :PyCharm
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 5, 16, 25]
# 变量fig表示整张图片，ax表示图片中的各个图表
fig, ax = plt.subplots()
ax.plot(input_value,squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签
ax.set_title("squares", fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("the value of squares",fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)
plt.show()
