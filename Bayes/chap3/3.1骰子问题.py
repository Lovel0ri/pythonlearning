# @Time: 2022/12/24 23:00
# @Author: 李树斌
# @File : 3.1骰子问题.py
# @Software :PyCharm
from thinkbayes2 import Suite


class Dice(Suite):


    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo



suite = Dice([4, 6, 8, 12, 20])
suite.Update(6)
for roll in [6, 8, 7, 7, 5, 4]:
    suite.Update(roll)
suite.Print()

