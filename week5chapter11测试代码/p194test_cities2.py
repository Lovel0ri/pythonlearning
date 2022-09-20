# @Time: 2022/9/20 11:03
# @Author: 李树斌
# @File : p194test_cities2.py
# @Software :PyCharm
import unittest
from P194练习2 import get_city_country

class Test_city_country(unittest.TestCase):
    def test_get_city_country(self):
        full_info = get_city_country('Guangzhou','China')
        self.assertEqual(full_info,'Guangzhou,China')

class Test_city_country2(unittest.TestCase):
    def test_get_city_country(self):
        full_info = get_city_country('Guangzhou','China','100')
        self.assertEqual(full_info,'Guangzhou,China - 100')

if __name__ == '__main__':
    unittest.main