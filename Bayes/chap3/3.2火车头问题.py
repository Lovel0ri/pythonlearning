# @Time: 2022/12/24 23:33
# @Author: 李树斌
# @File : 3.2火车头问题.py
# @Software :PyCharm
from thinkbayes2 import Suite
from thinkbayes2 import Pmf
from matplotlib import pyplot as plt


class Train(Suite):
    def __init__(self,hypos,alpha=1):
        Pmf.__init__(self)
        self.alpha = alpha
        for hypo in hypos:
            self.Set(hypo,hypo**(-alpha))
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo

def Mean(suite):
    total = 0
    for hypo, prob in suite.Items():
        print(hypo, prob)
        total += hypo * prob
    return total

hypos = range(1, 1001)
suite = Train(hypos)
suite.Update(60)
#画图
x = []
y = []
for hypo, prob in suite.Items():
    x.append(hypo)
    y.append(prob)
plt.plot(x, y)
# plt.show()
def Percentile(suite, percentage):
    p = percentage / 100.0
    total = 0
    for value, prob in sorted(suite.Items()):
        total += prob
        if total >= p:
            return value
interval = Percentile(suite, 5), Percentile(suite, 95)
print(interval)