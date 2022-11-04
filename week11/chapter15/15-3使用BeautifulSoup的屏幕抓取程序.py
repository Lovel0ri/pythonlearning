# @Time: 2022/11/4 16:58
# @Author: 李树斌
# @File : 15-3使用BeautifulSoup的屏幕抓取程序.py
# @Software :PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('http://python.org/jobs').read()
soup = BeautifulSoup(text,'html.parser')

jobs = set()
# for job in soup.body.section("h2"):
#     jobs.add(('{}({})').format(job.a.string,job.a['href']))
#
# print('\n'.join(sorted(jobs,key = str.lower)))
for i in range(1,4):
    for job in soup.body.section("h2"):
        jobs.add((f"{job.a.string}({job.a['href']})"))

print('\n'.join(sorted(jobs,key = str.lower)))
#print(soup.body.section("h2"))