# @Time: 2022/11/9 13:51
# @Author: 李树斌
# @File : 建立由列表组成的列表.py
# @Software :PyCharm
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)


werid_board = [['_'] * 3] * 3
werid_board[1][2] = 'O'
print(werid_board)