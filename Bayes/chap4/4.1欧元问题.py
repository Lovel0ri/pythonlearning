# @Time: 2022/12/25 0:22
# @Author: 李树斌
# @File : 4.1欧元问题.py
# @Software :PyCharm
from thinkbayes2 import Suite
class Euro(Suite):
    def Likelihood(self, data, hypo):
        if data == 'H':
            return hypo/100.0
        else:
            return 1-hypo/100.0

suite = Euro(range(0, 101))
dataset = 'H' * 140 + 'T' * 110
for data in dataset:
    suite.Update(data)

#画图
import matplotlib.pyplot as plt
x = []
y = []
for hypo, prob in suite.Items():
    x.append(hypo)
    y.append(prob)
plt.plot(x, y)
plt.show()