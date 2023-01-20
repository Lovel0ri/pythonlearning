# @Time: 2022/12/25 21:57
# @Author: 李树斌
# @File : 5.4加速.py
# @Software :PyCharm
import thinkbayes2
from thinkbayes2 import Pmf

class Die(Pmf):
    def __init__(self, sides):
        Pmf.__init__(self)
        for x in range(1, sides+1):
            self.Set(x, 1)
        self.Normalize()
    #
    # def Likelihood(self, data, hypo):
    #     if hypo < data:
    #         return 0
    #     else:
    #         return 1.0/hypo

d6 = Die(6)
dice = [d6] * 3
three = thinkbayes2.SampleSum(dice,1000)
print(three)