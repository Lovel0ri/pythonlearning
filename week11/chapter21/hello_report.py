# @Time: 2022/11/6 16:09
# @Author: 李树斌
# @File : hello_report.py
# @Software :PyCharm

from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50,50,'Hello,world!',textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d,'hello.pdf','A simple PDF file')