# @Time: 2022/9/20 13:33
# @Author: 李树斌
# @File : p200test_Empolyee.py
# @Software :PyCharm
import unittest
from employeep200 import Employee

class Test_Employee(unittest.TestCase):
    def setUp(self) -> None:
        self.my_info = Employee('Bingbing','Chen',1000)
        self.increase = 1000

    def test_give_default_raise(self):
        self.my_info.give_raise()

    def test_give_custom_raise(self):
        self.my_info.give_raise(self.increase)

if __name__ == '__main__':
    unittest.main