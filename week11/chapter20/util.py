# @Time: 2022/11/6 15:21
# @Author: 李树斌
# @File : util.py
# @Software :PyCharm
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


