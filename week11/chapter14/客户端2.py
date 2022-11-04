# @Time: 2022/11/3 19:52
# @Author: 李树斌
# @File : 客户端2.py
# @Software :PyCharm
import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

s.connect((host, port))
print(s.recv(1024))