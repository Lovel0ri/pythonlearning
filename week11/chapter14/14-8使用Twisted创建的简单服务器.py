# @Time: 2022/11/4 13:48
# @Author: 李树斌
# @File : 14-8使用Twisted创建的简单服务器.py
# @Software :PyCharm
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver
class SimpleLogger(LineReceiver):
    def connectionMade(self):
        print("Got connection from", self.transport.client)

    def connectionLost(self,reason):
        print(self.transport.client, "disconnected")

    def lineReceived(self, line):
        print(line)

# 创建工厂
factory = Factory()
# 指定协议
factory.protocol = SimpleLogger

reactor.listenTCP(12345, factory)
reactor.run()