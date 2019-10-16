#!/usr/bin/python
#-*-coding:utf8-*-
#客户端
#客户端不需要绑定ip和监听
import socket
while True:
    #创建一个套件
    sock=socket.socket()
    #客户端虽然不需要绑定Ip,但是连接服务器
    sock.connect(('192.168.2.137',808))
    #发送请求
    #请求的内容
    message=input('请输入请求内容：')
    #发送请求的内容给服务器
    sock.send(message.encode('utf8'))
    #接收服务器的响应
    recive=sock.recv(1024)
    print(recive.decode('utf8'))
    #断开连接
    sock.close()