# @Time: 2022/11/6 16:43
# @Author: 李树斌
# @File : 包含一些清理代码的基本服务器.py
# @Software :PyCharm
from asyncore import dispatcher
import asyncore,socket

PORT = 5005

# 服务器类
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

    def handle_accept(self) -> None:
        conn, addr = self.accept()
        print("Connection attempt from", addr[0])


if __name__ == "__main__":
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:pass
