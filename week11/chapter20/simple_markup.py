# @Time: 2022/11/6 15:44
# @Author: 李树斌
# @File : simple_markup.py
# @Software :PyCharm
import sys,re
from util import *
print('<html><head><title>...</title><body>')
file_name  = 'test_input.txt'
title = True
for block in blocks(file_name):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')


print('</body></html>')