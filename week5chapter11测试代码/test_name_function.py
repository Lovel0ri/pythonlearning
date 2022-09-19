# @Time: 2022/9/20 1:39
# @Author: 李树斌
# @File : test_name_function.py
# @Software :PyCharm
import unittest
from name_function import get_formatted_name
#不要修改测试，应该修改测试不通过的代码
class NamesTestCase(unittest.TestCase):

     def test_first_last_name(self):
         formatted_name = get_formatted_name('Bingbing','Chen')
         self.assertEqual(formatted_name,'Bingbing Chen')

if __name__ == '__main__':
    unittest.main
