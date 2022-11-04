# @Time: 2022/11/3 19:12
# @Author: 李树斌
# @File : 14-1最简单的服务器.py
# @Software :PyCharm
import socket
s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send("Thank you for connecting".encode())
    c.close()