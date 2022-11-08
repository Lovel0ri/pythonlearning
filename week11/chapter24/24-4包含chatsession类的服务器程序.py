# @Time: 2022/11/8 12:48
# @Author: 李树斌
# @File : 24-4包含chatsession类的服务器程序.py
# @Software :PyCharm
from asyncore import dispatcher
from asynchat import async_chat
import asyncore,socket

PORT = 5005

# 服务器类
class ChatSession(async_chat):
    def __init__(self,sock):
        async_chat. init(self,sock)
        #self.server = server
        self.set_terminator("\r\n")
        self.data = []
        #self.push(b"Welcome to the chatroom\r")

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = "".join(self.data)
        self.data = []
        print(line)

class ChatServer(dispatcher):
    def __init__(self, port):
        # 初始化父类
        dispatcher.__init__(self)
        # 创建套接字
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定端口
        self.set_reuse_addr()
        # 绑定端口
        self.bind(("", port))
        self.listen(5)
        self.sessions = []

    def handle_accept(self) -> None:
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn))


if __name__ == "__main__":
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:print()