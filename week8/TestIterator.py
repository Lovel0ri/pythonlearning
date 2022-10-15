# @Time: 2022/10/15 15:35
# @Author: 李树斌
# @File : TestIterator.py
# @Software :PyCharm
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))
print(list(ti))
