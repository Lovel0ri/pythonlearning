# @Time: 2022/11/6 16:29
# @Author: 李树斌
# @File : 极简的服务器程序.py
# @Software :PyCharm
from asyncore import dispatcher
import asyncore

# 服务器类
class ChatServer(dispatcher):
    def handle_accept(self) -> None:
        conn, addr = self.accept()
        print("Connection attempt from", addr[0])


# 服务器端口
s = ChatServer()
s = create_server(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 5005))
# 监听
s.listen(5)
# 服务器一直运行
asyncore.loop()