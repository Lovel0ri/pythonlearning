# @Time: 2022/9/20 13:54
# @Author: 李树斌
# @File : github0.py
# @Software :PyCharm
import unittest
"""测试代码"""
class Employee(unittest.TestCase):
    def setUp(self) -> None:
        self.my_info = Employee('Bingbing','Chen',1000)
        self.increase = 1000

    def give_default_raise(self):
        self.my_info.give_raise()

if __name__ == '__main__':
    unittest.main