# @Time: 2022/10/1 14:24
# @Author: 李树斌
# @File : 断言结束while循环.py
# @Software :PyCharm
while True:
    word = input('Please enter a word: ')
    if not word:
        break
    print('The word was', word)