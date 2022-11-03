# @Time: 2022/11/3 16:53
# @Author: 李树斌
# @File : importdata.py
# @Software :PyCharm
import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()