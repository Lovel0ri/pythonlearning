# @Time: 2022/11/3 19:51
# @Author: 李树斌
# @File : 14-5线程化服务器.py
# @Software :PyCharm
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

# 服务器端
class Server(ThreadingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    # 重写handle方法
    def handle(self):
        # 获取客户端的ip和端口
        addr = self.request.getpeername()
        print("Got connection from", addr)
        self.wfile.write("HELLO!".encode())

# 创建服务器
sever = Server(("", 12345), Handler)
# 启动服务器
sever.serve_forever()