# @Time: 2022/9/20 10:46
# @Author: 李树斌
# @File : p194test_cities.py
# @Software :PyCharm
import unittest
from p194练习 import get_city_country

class Test_city_country(unittest.TestCase):
    def test_get_city_country(self):
        full_info = get_city_country('Guangzhou','China')
        self.assertEqual(full_info,'Guangzhou,China')

if __name__ == '__main__':
    unittest.main