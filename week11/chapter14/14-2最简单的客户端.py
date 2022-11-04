# @Time: 2022/11/3 19:13
# @Author: 李树斌
# @File : 14-2最简单的客户端.py
# @Software :PyCharm
import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

s.connect((host, port))
print(s.recv(1024))