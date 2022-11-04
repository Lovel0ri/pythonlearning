# @Time: 2022/11/4 13:19
# @Author: 李树斌
# @File : 14-6使用select的简单服务器.py
# @Software :PyCharm
import socket,select

s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
# 创建一个空的列表，用来存放客户端的socket
input([s])
while True:
    rs, ws, es = select.select(input,[],[])
    for r in rs:
        # 如果是服务器的socket，说明有新的客户端连接
        if r is s:
            c, addr = s.accept()
            print("Got connection from", addr)
            # 将客户端的socket加入到列表中
            input.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print(r.getpeername(), 'disconnected')
                input.remove(r)
            else:
                print(data)