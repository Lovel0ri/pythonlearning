# @Time: 2022/12/26 19:00
# @Author: 李树斌
# @File : BingoCage.py
# @Software :PyCharm
import random
class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(10))
print(bingo())